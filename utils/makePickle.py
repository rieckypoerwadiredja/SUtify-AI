import pickle
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize

def makePickel(dir,classifier):
    with open(dir, 'wb') as file:
        pickle.dump(classifier, file)
    
        