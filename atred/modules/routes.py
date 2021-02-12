import re
from atred.modules.general import prepare_message
from atred.modules.models.__main__ import load_models

models = load_models()

def check_route(regex, route):
    found = False

    if re.search(regex, route) != None:
        found = True
    
    return found

def prepare_route(route, data = [], model=''):
    response = ''

    if model == None:
        model = ''

    if check_route("^\/?summarize$", route):
        try:
            response = models["nlp"]["summarization"](model=model, content=data)
            
            return prepare_message(content=response)
        except:
            return prepare_message(code=500, message=f"Input must have more than one sentence")
    elif check_route("^\/?sentiment$", route):
        try:
            response = models["nlp"]["sentiment"](model=model, content=data)

            return prepare_message(content=response)
        except:
            return prepare_message(code=500, message=f"Input must have more than one sentence")
    else:
        return prepare_message(code=404, message=f"The '{route}' path doesn't exist.")