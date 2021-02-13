# LOAD MODULES
from atred.modules.models.nlp.summarization import summarize
from atred.modules.models.nlp.entity import find_entities
from atred.modules.models.nlp.sentiment import predict_sentiment

def load_models():
    return {
        "nlp": {
            "summarization": summarize,
            "entity": find_entities,
            "sentiment": predict_sentiment,
        }
    }