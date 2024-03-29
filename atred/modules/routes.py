import re
from atred.modules.general import prepare_message
from atred.modules.models.__main__ import load_models
from atred.modules.general import first_available_key

models = load_models()

def check_route(regex, route):
    found = False

    if re.search(regex, route) != None:
        found = True
    
    return found

def prepare_route(route, data = [], model='', options=None):
    response = ''

    if model == None:
        model = ''

    if options == None:
        options = {}

    limit = first_available_key([ "count", "limit" ], options)
    whole_content = first_available_key([ "whole_content", "whole", "total_content", "total" ], options)
    if limit == None:
        limit = 0
    if whole_content == None:
        whole_content = False

    try:
        if check_route("^\/?summarize$", route):
            response = models["nlp"]["summarization"](model=model, content=data)
        elif check_route("^\/?entity$", route):
            response = models["nlp"]["entity"](model=model, content=data)
        elif check_route("^\/?sentiment$", route):
            response = models["nlp"]["sentiment"](model=model, content=data)
        elif check_route("^\/?aspect[_\-\. ]+sentiment$", route):
            response = models["nlp"]["aspect_sentiment"](model=model, content=data, count=limit, whole=whole_content)
        elif check_route("^\/?classify$", route):
            response = models["nlp"]["classify"](model=model, content=data)
        elif check_route("^\/?vocabulary$", route):
            response = models["nlp"]["vocabulary"](model=model, content=data, count=limit)
        else:
            return prepare_message(code=404, message=f"The '{route}' path doesn't exist.")

        if response != '':
            return prepare_message(content=response)
    except:
        return prepare_message(code=500, message=f"Input must have more than one sentence")