## LOAD MODULES
from atred.modules.models.nlp.sentiment import bart_base_multilingual_uncased_sentiment_prediction
from atred.modules.models.nlp.summarization import spacy_en_core_web_sm_summarize, gensim_summarization

def load_models():
    return {
        "nlp": {
            "spacy": {
                "summarization": {
                    "summarize": spacy_en_core_web_sm_summarize
                }
            },
            "gensim": {
                "summarization": {
                    "summarize": gensim_summarization.summarize
                }
            },
            "bert": {
                "sentiment": {
                    "multilingual": bart_base_multilingual_uncased_sentiment_prediction
                }
            }
        }
    }