## LOAD MODULES
import pickle
from sklearn.feature_extraction.text import CountVectorizer

# LOAD MODELS
softmax_vectors = CountVectorizer(vocabulary=pickle.load(open("atred/modules/models/nlp/classifier/news/vectors.pkl", "rb")))
softmax_vectors_frequency = pickle.load(open("atred/modules/models/nlp/classifier/news/vectors_frequency.pkl","rb"))
softmax_model = pickle.load(open("atred/modules/models/nlp/classifier/news/model.pkl","rb"))

def classify(model="softmax", content=""):
    normalized_content = content

    if isinstance(content, list) == False:
        normalized_content = [content]

    predicted_categories = []

    validated_model_name = model.lower()

    if model.lower() == "":
        validated_model_name = "softmax"

    if validated_model_name == "softmax":
        category_list = ["sport", "world", "us", "business", "health", "entertainment", "sci_tech"]
        x_vectors = softmax_vectors.transform(normalized_content)
        x_vectors_frequency = softmax_vectors_frequency.transform(x_vectors)
        predicted = softmax_model.predict(x_vectors_frequency)
        
        for index, predictedRow in enumerate(predicted):
            predicted_categories.append({
                "sentence": normalized_content[index],
                "category": category_list[predictedRow],
            })

    return predicted_categories