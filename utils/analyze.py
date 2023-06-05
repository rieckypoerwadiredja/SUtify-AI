import pickle
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize

def analyzeReview(dir,cek):
    classifier_file = open(dir,"rb")
    try:
        classifier = pickle.load(classifier_file)
        if classifier:
            pass
        else: 
            print("The Pickle file is empty, please enter the results of the analysis first")
            return
    except:
        print("The Pickle file is empty, please enter the results of the analysis first")
        return
    classifier_file.close()
        
    res = classifier.classify(FreqDist(word_tokenize(cek)))
    print(cek,"-->" ,res)