# NLTK
from nltk import word_tokenize, sent_tokenize
from nltk.probability import FreqDist

# Utils
from utils.cleaners import indexCleaner
from utils.plot import plot
from utils.analyze import analyze, analyze_sentence
from utils.readFile import readCsv
from utils.classify import classify, classify_sentence


def getWord(dataset):
    # TODO: Get Word from text
    review = dataset['Review']
    label = dataset['Label']
    
    # TODO: Mengambil kata2 dari databse dengan memberikan label (positive / negative)
    wordsLabel = []
    for rev, lab in zip(review, label):
        if lab == 1:
            lab = 'positive'
        if lab == 0:
            lab = 'negative'
        word = word_tokenize(rev)
        wordsLabel.append((word, lab))

    # print(wordsLabel[0][0])
    
    # TODO: Memisahkan kata dalam kalimat berdasarkan jenisnya
    positiveWords = []
    negativeWords = []
    
    for index, data in enumerate(wordsLabel):
        # print(wordsLabel[index][0]) # Dapet data pertama
        for word in wordsLabel[index][0]:
            if wordsLabel[index][1] == 'positive':
                positiveWords.append(word)
            if wordsLabel[index][1] == 'negative':
                negativeWords.append(word)
   
    # TODO: Ambil kata unik
    all_unik_positive_words = FreqDist(positiveWords).keys()
    print(all_unik_positive_words)
    
    # TODO: Clean Word
    cleanPositiveWord = indexCleaner(all_unik_positive_words)
    
    # TODO: Ambil kata unik
    all_unik_negative_words = FreqDist(positiveWords).keys()
    
    # TODO: Clean Word
    cleanNegativeWord = indexCleaner(all_unik_negative_words)
    
    words = []
    # TODO: Membari label tiap jenis
    for word in cleanPositiveWord:
        words.append((word,"positive"))
    for word in cleanNegativeWord:
        words.append((word,"negative"))
    # print(words)
    return words
    
def getSent(dataset):
     # TODO: Get Sent from text     
    sents = dataset['Review']

    # TODO: Ambil kata unik
    all_unik_sents = FreqDist(sents).keys()
    # print(all_unik_sents)
    
    # TODO: Clean Word
    cleanSent = indexCleaner(all_unik_sents)
    feature_set = getWord(dataset)
    print(feature_set)
    
    # TODO: Traning & testing
    import random
    
    random.shuffle(feature_set)
    train_count = int(len(feature_set)*0.9) # Mengambil 9 dari 10 dataset
    train_data = feature_set[:train_count] 
    test_data = feature_set[train_count:]
    
    from  nltk.classify import NaiveBayesClassifier, accuracy
    
    classifier = NaiveBayesClassifier.train(train_data)
    classifier.show_most_informative_features(10)
    print(accuracy(classifier, test_data)*100)   
