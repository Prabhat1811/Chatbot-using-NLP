import nltk

# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('omw-1.4')
# nltk.download('wordnet')
# nltk.download('book')

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.book import *
from nltk import FreqDist

'''
TOKENIZING
'''
example_string = "The crew of the USS Discovery discovered many discoveries. Discovering is what explorers do."

tokenized_words = word_tokenize(example_string)

stop_words = set(stopwords.words("english"))

filtered_list = []

for word in tokenized_words:
    if word.casefold() not in stop_words:
        filtered_list.append(word)

# print(filtered_list)


'''
STEMMING
'''
stemmer = PorterStemmer()

stemmed_words = [stemmer.stem(word) for word in filtered_list]

# print(stemmed_words)


'''
POS Tagging

JJ - Adjective
NN - Noun
RB - Adverb
PRP - Pronoun
VB - Verb
'''

tagged_words = nltk.pos_tag(filtered_list)
# print(tagged_words)


'''
Lemmatizing
'''
lemmatizer = WordNetLemmatizer()

# print(lemmatizer.lemmatize('text'))


'''
Dispersion Plot
'''
# text8.dispersion_plot(["women", "man"])


'''
Frequency Distribution
'''
meaningfull_words = [word for word in text8 if word.casefold() not in stop_words]

frequency_distribution = FreqDist(meaningfull_words)

frequency_distribution.plot(20, cumulative=True)







