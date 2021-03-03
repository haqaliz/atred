# LOAD MODULES
from atred.modules.models.nlp.summarization import summarize
from atred.modules.models.nlp.entity import find_entities
from atred.modules.models.nlp.sentiment import predict_sentiment
from atred.modules.models.nlp.classifier.news import classify
from atred.modules.models.nlp.terminology import vocabulary

def load_models():
    return {
        "nlp": {
            "summarization": summarize,
            "entity": find_entities,
            "sentiment": predict_sentiment,
            "classify": classify,
            "vocabulary": vocabulary,
        }
    }