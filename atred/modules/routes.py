import re
from atred.modules.general import prepare_message
from atred.modules.models.__main__ import load_models

models = load_models()

def check_route(regex, route):
    found = False

    if re.search(regex, route) != None:
        found = True
    
    return found

def prepare_route(route, data = []):
    if check_route("^\/?hello$", route):
        try:
            gensim_summarize = models["nlp"]["gensim"]["summarization"]["summarize"]
            spacy_summarize = models["nlp"]["spacy"]["summarization"]["summarize"]
            summarized_by_gensim = gensim_summarize(data)
            summarized_by_spacy = spacy_summarize(data)
            response = ''

            if (len(response) == 0 and len(summarized_by_gensim) > 0) or (len(response) > 0 and len(summarized_by_gensim) < len(response)):
                response = summarized_by_gensim

            if (len(summarized_by_spacy) == 0 and len(summarized_by_spacy) > 0) or (len(response) > 0 and len(summarized_by_spacy) < len(response)):
                response = summarized_by_spacy

            return prepare_message(content=response)
        except:
            return prepare_message(code=500, message=f"Input must have more than one sentence")
    else:
        return prepare_message(code=404, message=f"The '{route}' path doesn't exist.")