def prepare_message(code = 200, message = '', content = {}):
    response_content = {
        "meta": {
            "code": code
        }
    }

    if code == 200:
        response_content["meta"]["content"] = content
    else:
        response_content["meta"]["message"] = message

    return response_content

def check_keys_existence(keys = [], dictionary = {}):
    if isinstance(keys, str):
        keys = map(lambda key: key.strip(), keys.split(",")) 

    result = True

    for key in keys:
        if key not in dictionary:
            result = False
            break
    
    return result

def first_available_key(keys = [], dictionary = {}):
    if isinstance(keys, str):
        keys = map(lambda key: key.strip(), keys.split(",")) 

    result = None

    for key in keys:
        if key in dictionary:
            result = dictionary[key]
            break

    return result