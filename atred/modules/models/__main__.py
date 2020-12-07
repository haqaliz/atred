import spacy
import gensim
from spacy.lang.en.stop_words import STOP_WORDS

from string import punctuation
from heapq import nlargest

en_core_web_sm_nlp = spacy.load('en_core_web_sm')
gensim_summarization = gensim.summarization

def summarize(raw_docx):
    raw_text = raw_docx
    docx = en_core_web_sm_nlp(raw_text)
    stopwords = list(STOP_WORDS)
    word_frequencies = {}

    for word in docx:  
        if word.text not in stopwords:
            if word.text not in word_frequencies.keys():
                word_frequencies[word.text] = 1
            else:
                word_frequencies[word.text] += 1

    maximum_frequncy = max(word_frequencies.values())

    for word in word_frequencies.keys():  
        word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)

    sentence_list = [ sentence for sentence in docx.sents ]
    sentence_scores = {}  

    for sent in sentence_list:  
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if len(sent.text.split(' ')) < 30:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word.text.lower()]
                    else:
                        sentence_scores[sent] += word_frequencies[word.text.lower()]

    summarized_sentences = nlargest(7, sentence_scores, key=sentence_scores.get)
    final_sentences = [ w.text for w in summarized_sentences ]
    summary = ' '.join(final_sentences)

    return summary

def load_models():
    return {
        "nlp": {
            "spacy": {
                "summarization": {
                    "summarize": summarize
                }
            },
            "gensim": {
                "summarization": {
                    "summarize": gensim_summarization.summarize
                }
            }
        }
    }