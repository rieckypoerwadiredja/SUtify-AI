# NLTK
from nltk import word_tokenize
from nltk.probability import FreqDist

# Utils
from utils.cleaners import indexCleaner
from utils.makePickle import makePickel


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

    print(wordsLabel)
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
    all_unik_positive_words = FreqDist(positiveWords)
    # print("Kotor pos",len(all_unik_positive_words))
    # TODO: Clean Word
    cleanPositiveWord = indexCleaner(all_unik_positive_words)
    # print("bersih pos",len(cleanPositiveWord))
    
    # TODO: Ambil kata unik
    all_unik_negative_words = FreqDist(positiveWords)
    # print("kotor neg",len(all_unik_negative_words))
    
    # TODO: Clean Word
    cleanNegativeWord = indexCleaner(all_unik_negative_words)
    # print("kotor neg",len(cleanNegativeWord))
    
    words = []
    # TODO: Membari label tiap jenis
    for word in cleanPositiveWord:
        words.append(({word:True},"positive"))
    for word in cleanNegativeWord:
        words.append(({word:True},"negative"))
    # print(words)
    return words
    
def getAnalyzeResult(dataset):
    feature_set = getWord(dataset)
    # print(feature_set)
    
    # # TODO: Traning & testing
    import random
    
    random.shuffle(feature_set)
    train_count = int(len(feature_set)*0.9) # Mengambil 9 dari 10 dataset
    train_data = feature_set[:train_count] # Mengambil dara dari awal smp ke limit untuk train data
    test_data = feature_set[train_count:] # Mengambil mengambil dari sisa (limit data traning smp selesai)
    
    from  nltk.classify import NaiveBayesClassifier, accuracy
    
    classifier = NaiveBayesClassifier.train(train_data)
    classifier.show_most_informative_features(10)
    print(accuracy(classifier, test_data)*100)   
    
    makePickel('./model/model.pickle',classifier)
    
