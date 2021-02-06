## LOAD MODULES
from adaptnlp import TransformersSequenceClassifier

## LOAD MODELS
bart_base_multilingual_uncased_sentiment = TransformersSequenceClassifier.load("nlptown/bert-base-multilingual-uncased-sentiment")

def bart_base_multilingual_uncased_sentiment_prediction(content, mini_batch_size = 2):
    normalized_content = content

    if isinstance(content, list) == False:
        normalized_content = [content]

    sentences = bart_base_multilingual_uncased_sentiment.predict(text = normalized_content, mini_batch_size = mini_batch_size)
    sentences_predictions = []
            
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
        
    return sentences_predictions
      