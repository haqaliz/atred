# NLP Pkgs
import spacy 
nlp = spacy.load('en')
# Pkgs for Normalizing Text
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
# Finding the Top N Sentences
from heapq import nlargest



def text_summarizer(raw_docx):
    """ usage: text_summarizer(yourtext) """
    raw_text = raw_docx
    docx = nlp(raw_text)
    stopwords = list(STOP_WORDS)
    # Build Word Frequency # word.text is tokenization in spacy
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
    # Sentence Tokens
    sentence_list = [ sentence for sentence in docx.sents ]

    #Calculate Sentence Scores
    sentence_scores = {}  
    for sent in sentence_list:  
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if len(sent.text.split(' ')) < 30:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word.text.lower()]
                    else:
                        sentence_scores[sent] += word_frequencies[word.text.lower()]

    # Find N Largest and Join Sentences
    summarized_sentences = nlargest(7, sentence_scores, key=sentence_scores.get)
    final_sentences = [ w.text for w in summarized_sentences ]
    summary = ' '.join(final_sentences)
    print("Original Document\n")
    print(raw_docx)
    print("Total Length:",len(raw_docx))
    print('\n\nSummarized Document\n')
    print(summary)
    print("Total Length:",len(summary))

test = """In an attempt to build an AI-ready workforce, Microsoft announced Intelligent Cloud Hub which has been launched to empower
the next generation of students with AI-ready skills. Envisioned as a three-year collaborative program, Intelligent Cloud Hub will 
support around 100 institutions with AI infrastructure, course content and curriculum, developer support, development tools and give 
students access to cloud and AI services. As part of the program, the Redmond giant which wants to expand its reach and is planning to 
build a strong developer ecosystem in India with the program will set up the core AI infrastructure and IoT Hub for the selected campuses. 
The company will provide AI development tools and Azure AI services such as Microsoft Cognitive Services, Bot Services and Azure Machine 
Learning.According to Manish Prakash, Country General Manager-PS, Health and Education, Microsoft India, said, "With AI being the defining 
technology of our time, it is transforming lives and industry and the jobs of tomorrow will require a different skillset. This will require more 
collaborations and training and working with AI. That’s why it has become more critical than ever for educational institutions to integrate new 
cloud and AI technologies. The program is an attempt to ramp up the institutional set-up and build capabilities among the educators to educate 
the workforce of tomorrow." The program aims to build up the cognitive skills and in-depth understanding of developing intelligent cloud connected 
solutions for applications across industry. Earlier in April this year, the company announced Microsoft Professional Program In AI as a learning 
track open to the public. The program was developed to provide job ready skills to programmers who wanted to hone their skills in AI and data science 
with a series of online courses which featured hands-on labs and expert instructors as well. This program also included developer-focused AI 
school that provided a bunch of assets to help build AI skills."""

text_summarizer(test)

from gensim.summarization import summarize
print("=================")
gsum = summarize(test)
print(gsum)
print(len(gsum))