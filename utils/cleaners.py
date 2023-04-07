# python
import string
# NLTK
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

def indexCleaner(wordList = []):
    cleanWord = deletePunctuation(wordList)
    cleanWord = deleteStopWord(cleanWord)
    cleanWord = snowballStemmer(cleanWord)
    return cleanWord

def deletePunctuation(wordList = []):
    punctuation_list = string.punctuation
    cleanWord = []
    if len(wordList) < 1:
        print("<!> Error 'wordList' data tidak valid")
    for word in wordList:
        if word not in punctuation_list:
            cleanWord.append(word)
    return cleanWord


def deleteStopWord(wordList = []):
    stopword_list = stopwords.words('english')
    cleanWord = []
    if len(wordList) < 1:
        print("<!> Error 'wordList' data tidak valid")
    for word in wordList:
        if word not in stopword_list:
            cleanWord.append(word)
    return cleanWord

def snowballStemmer(wordList = []):
    snowball_stemmer = SnowballStemmer('english')
    cleanWord = []
    if len(wordList) < 1:
        print("<!> Error 'wordList' data tidak valid")
    for word in wordList:
        snowballStemmerWord = snowball_stemmer.stem(word)
        cleanWord.append(snowballStemmerWord)
        
    return cleanWord