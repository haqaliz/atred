## LOAD MODULES
import spacy

## LOAD MODELS
en_core_web_sm_entity = spacy.load('en_core_web_sm')

def find_entities(model="spacy/en_core_web_sm", content="", mini_batch_size = 2):
    normalized_content = content

    if isinstance(content, list) == True:
        normalized_content = ' '.join(content)

    validated_model_name = model.lower()

    if model.lower() == "":
        validated_model_name = "spacy/en_core_web_sm"

    entities = []
    
    if validated_model_name == "spacy/en_core_web_sm":
        text_content= en_core_web_sm_entity(normalized_content)
        for entity in text_content:
            if entity.ent_type_ != "":
                entities.append({
                    "entity": entity.text,
                    "label": {
                        "key": entity.ent_type_,
                        "lemma": entity.lemma_,
                        "position": entity.pos_,
                        "tag": entity.tag_,
                        "dependency": entity.dep_,
                        "shape": entity.shape_,
                        "is_alphabetic": entity.is_alpha,
                        "is_stop_word": entity.is_stop,
                    },
                })
        
    return entities
