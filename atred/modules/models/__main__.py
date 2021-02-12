# LOAD MODULES
from atred.modules.models.nlp.sentiment import predict_sentiment
from atred.modules.models.nlp.summarization import summarize

def load_models():
    return {
        "nlp": {
            "summarization": summarize,
            "sentiment": predict_sentiment
        }
    }


# from adaptnlp import EasyTokenTagger 
# ## Example Text 
# example_text = "An expert from a World Health Organization team investigating the origins of Covid-19 on the ground in China has lashed out at US President Joe Biden for posturing against Beijing, and taken a shot at the credibility of US intelligence agencies after the State Department expressed uncertainty over the team's initial findings."
# ## Load the token tagger module and tag text with the NER model
# tagger = EasyTokenTagger()
# sentences = tagger.tag_text(text=example_text, model_name_or_path="ner") 
# ## Output tagged token span results in Flair’s Sentence object model
# for sentence in sentences: 
#     for entity in sentence.get_spans("ner"): 
#         print(entity)


# from spacy import displacy
# import en_core_web_sm
# nlp = en_core_web_sm.load()
# example_text = "An expert from a World Health Organization team investigating the origins of Covid-19 on the ground in China has lashed out at US President Joe Biden for posturing against Beijing, and taken a shot at the credibility of US intelligence agencies after the State Department expressed uncertainty over the team's initial findings."
# text_content= nlp(example_text)
# entities=[(i, i.label_, i.label) for i in text_content.ents]
# print(entities)