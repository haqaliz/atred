## LOAD MODULES
from adaptnlp import TransformersSequenceClassifier
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TextClassificationPipeline

## LOAD MODELS
bart_base_multilingual_uncased_sentiment = TransformersSequenceClassifier.load("nlptown/bert-base-multilingual-uncased-sentiment")
distilbert_base_uncased_finetuned_sst2_english_tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
distilbert_base_uncased_finetuned_sst2_english_model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
distilbert_base_uncased_finetuned_sst2_english_predictor = TextClassificationPipeline('sentiment-analysis', model=distilbert_base_uncased_finetuned_sst2_english_model, tokenizer=distilbert_base_uncased_finetuned_sst2_english_tokenizer)

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
