## LOAD MODULES
from adaptnlp import TransformersSequenceClassifier
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TextClassificationPipeline
import aspect_based_sentiment_analysis as absa
from atred.modules.models.nlp.terminology import vocabulary

## LOAD MODELS
bart_base_multilingual_uncased_sentiment = TransformersSequenceClassifier.load("nlptown/bert-base-multilingual-uncased-sentiment")
distilbert_base_uncased_finetuned_sst2_english_tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
distilbert_base_uncased_finetuned_sst2_english_model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
distilbert_base_uncased_finetuned_sst2_english_predictor = TextClassificationPipeline('sentiment-analysis', model=distilbert_base_uncased_finetuned_sst2_english_model, tokenizer=distilbert_base_uncased_finetuned_sst2_english_tokenizer)
aspect_based_sentiment_analysis_model = absa.load()

def predict_sentiment(model="nlptown/bert-base-multilingual-uncased-sentiment", content="", mini_batch_size = 2):
    normalized_content = content

    if isinstance(content, list) == False:
        normalized_content = [content]

    validated_model_name = model.lower()

    if model.lower() == "":
        validated_model_name = "nlptown/bert-base-multilingual-uncased-sentiment"

    sentences_predictions = []
    
    if validated_model_name == "nlptown/bert-base-multilingual-uncased-sentiment":
        sentences = bart_base_multilingual_uncased_sentiment.predict(text = normalized_content, mini_batch_size = mini_batch_size)
                
        for sentence in sentences:
            sentence_content = sentence.to_original_text()
            sentence_dict = sentence.to_dict()
            sentence_labels_dict = list(map(lambda row: {
                "key": row['value'],
                "probability": row['confidence']
            }, sentence_dict['labels']))

            sentences_predictions.append({
                "sentence": sentence_content,
                "predictions": sentence_labels_dict
            })
    elif validated_model_name == "distilbert-base-uncased-finetuned-sst-2-english":
        sentences_predictions = distilbert_base_uncased_finetuned_sst2_english_predictor(normalized_content)
        
    return sentences_predictions

def predict_terminologies_sentiment(model="nltk-en/aspect-based", content="", count=0, whole=False):
    normalized_content = content

    if isinstance(content, list) == True:
        normalized_content = ' '.join(content)

    validated_model_name = model.lower()

    if model.lower() == "":
        validated_model_name = "nltk-en/aspect-based"

    terminology_validated_model_name = validated_model_name.replace("/aspect-based", "")
    aspects = []
    analysis = []
    words_sentiment = []

    if (
        (validated_model_name == "nltk-en/aspect-based") or 
        (validated_model_name == "gensim/aspect-based") or
        (validated_model_name == "spacy/en_core_web_sm/aspect-based")
    ):
        selected_vocabs = vocabulary(model=terminology_validated_model_name, content=normalized_content, count=count)
        aspects = list(map(lambda word: word, selected_vocabs))

    if whole == True:
        analysis = aspect_based_sentiment_analysis_model(normalized_content, aspects=aspects)
    else:
        for sentence in normalized_content.split('.'):
            stripped_sentence = sentence.strip()
            if stripped_sentence != '':
                analysis.append({
                    "sentence": f"{stripped_sentence}.",
                    "content": aspect_based_sentiment_analysis_model(stripped_sentence, aspects=aspects)
                })

    for item in analysis:
        if 'sentence' in item:
            item_sentence = item['sentence']

            for sentence_item in item['content']:
                aspect_sentiment = 'POSITIVE'

                if sentence_item.sentiment == absa.Sentiment.negative:
                    aspect_sentiment = 'NEGATIVE'
                
                words_sentiment.append({
                    "sentence": item_sentence,
                    "aspect": sentence_item.aspect,
                    "sentiment": aspect_sentiment,
                })

        else:
            aspect_sentiment = 'POSITIVE'

            if item.sentiment == absa.Sentiment.negative:
                aspect_sentiment = 'NEGATIVE'

            words_sentiment.append({
                "aspect": item.aspect,
                "sentiment": aspect_sentiment,
            })

    return words_sentiment