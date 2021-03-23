## LOAD MODULES
import re
import collections
from gensim.parsing.preprocessing import remove_stopwords
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import spacy

## LOAD MODELS
nltk.download('stopwords')
all_nltk_stopwords = stopwords.words('english')
all_nltk_stopwords.extend([ '.', ',', ':', ';', '"', '\'', '`', '’', '“', '”', '’', 'a', 's', 've', 'the', '-' ])
sp = spacy.load('en_core_web_sm')
all_stopwords = sp.Defaults.stop_words
all_stopwords.update([ '.', ',', ':', ';', '"', '\'', '`', '’', '“', '”', '’', 'a', 's', 've', 'the', '-' ])

def vocabulary(model="nltk-en", content="", count=0):
    normalized_content = content

    if isinstance(content, list) == True:
        normalized_content = ' '.join(content)

    validated_model_name = model.lower()

    if model.lower() == "":
        validated_model_name = "nltk-en"

    words = []

    if validated_model_name == "nltk-en":
        text_tokens = word_tokenize(normalized_content)
        words = [word for word in text_tokens if not word.lower() in all_nltk_stopwords]
    elif validated_model_name == "gensim":
        filtered_sentence = remove_stopwords(normalized_content)
        filtered_sentence = re.sub(f'([\.,:;\"\'`’“”’]+| ?the| ?ve)', '', filtered_sentence.lower())
        words = filtered_sentence.split()
    elif validated_model_name == "spacy/en_core_web_sm":
        text_tokens = word_tokenize(normalized_content)
        words = [word for word in text_tokens if not word.lower() in all_stopwords]

    wordcount = {}
    for word in words:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
    word_counter = collections.Counter(wordcount)

    if count > 0:
        repeated_words = word_counter.most_common(count)
        repeated_words_json = {}
        for word in repeated_words:
            repeated_words_json[word[0]] = word[1]
        
        return repeated_words_json

    return word_counter