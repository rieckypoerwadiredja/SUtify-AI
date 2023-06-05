import pickle
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize

def analyzeReview(dir,cek):
    classifier_file = open(dir,"rb")
    classifier = pickle.load(classifier_file)
    classifier_file.close()
        
    res = classifier.classify(FreqDist(word_tokenize(cek)))
    print(cek,"-->" ,res)