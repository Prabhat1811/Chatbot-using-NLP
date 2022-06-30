from nltk import word_tokenize
from nltk.stem import PorterStemmer
import numpy as np
import nltk

#Package with pre-trained tokenizer
nltk.download('punkt')

stemmer = PorterStemmer()

def tokenize(sentence: str) -> list:
    '''
    Get tokenized words from a sentence
    '''
    return word_tokenize(sentence)

def stem(word: str) -> str:
    '''
    Get words their root form
    '''
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence: list, all_words: list):
    '''
    tokenized_sentence = ['hello', 'how', 'are', 'you']
    all_words = ['hi', 'hello', 'I', 'you', 'bye', 'thank', 'cool']
    returned_value = [   0,     1,      0,    1,     0,      0,       0  ]
    '''
    tokenized_sentence = [stem(word) for word in tokenized_sentence]

    bag = np.zeros(len(all_words), dtype=np.float32)
    for index, word in enumerate(all_words):
        if word in tokenized_sentence:
            bag[index] = 1.0
    
    return bag
    


tokenized_sentence = ['hello', 'how', 'are', 'you']
all_words = ['hi', 'hello', 'I', 'you', 'bye', 'thank', 'cool']

bag = bag_of_words(tokenized_sentence, all_words)
# print(bag)
