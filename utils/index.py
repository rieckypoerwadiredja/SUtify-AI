# NLTK
from nltk import word_tokenize, sent_tokenize
from nltk.probability import FreqDist

# Utils
from utils.cleaners import indexCleaner
from utils.analyze import analyze
from utils.readFile import readCsv
from utils.classify import classify_word

text = readCsv(['Review'],'./data/dataset.csv') 
text = text.tolist()

def getWord(text):
    # TODO: Get Word from text
    words = []
    for sent in text:
        word = word_tokenize(sent)
        words.append(word)
        
    # TODO: Merubah array dalam array ke 1 array
    flattened_words = []
    for wordArray in words:
        for word in wordArray:
            flattened_words.append(word)
            
    # TODO: Ambil kata unik
    all_unik_words = FreqDist(flattened_words).keys()
    
    # TODO: Clean Word
    cleanWord = indexCleaner(all_unik_words)
    # TODO: Analyze
    analyzeResult = analyze(cleanWord)
    # TODO: Classify words (positive, neutral, negative)
    negative_words, neutral_words, positive_words = classify_word(analyzeResult)
    # print(negative_words)
    # print(neutral_words)
    # print(positive_words)
    return negative_words, neutral_words, positive_words

def getSent(dataset,text):
    # TODO: Classify words (positive, neutral, negative)
    sents = []
    for review, label in zip(dataset['Review'], dataset['Label']):
        sentiment = "positif" if label == 1 else "negatif"
        sent = (review,sentiment)
        sents.append(sent)
    # print(sents)
    
    # TODO: Mengambil nilai kata berdasarkan makna positif dan negatif
    negative_words, neutral_words, positive_words = getWord(text)
    feature_set = []
    for negative_word in negative_words:
        feature_set.append((negative_word['word'], 'negative'))

    for neutral_word in neutral_words:
        feature_set.append((neutral_word['word'], 'neutral'))

    for positive_word in positive_words:
        feature_set.append((positive_word['word'], 'positive'))
    print(feature_set)
    # TODO: Traning & testing
    import random
    from nltk.classify import NaiveBayesClassifier, accuracy

    # random.shuffle(feature_set)
    # train_count = int(len(feature_set) * 0.8)
    # train_data = feature_set[:train_count]
    # test_data = feature_set[train_count:]

    # # Training classifier
    # classifier = NaiveBayesClassifier.train(train_data)

    # # most informative features
    # classifier.show_most_informative_features(10)

    # # Testing accuracy
    # accuracy = accuracy(classifier, test_data) * 100
    # # print("Accuracy:", accuracy)
    from nltk.classify import NaiveBayesClassifier

    # Data training
    train_data = [
        ({'alright': 'positif', 'hope': 'positif', 'clear': 'positif', 'perfect': 'positif', 'wise': 'positif', 'entertain': 'positif', 'love': 'positif'}, 'positif'),
        ({'road': 'netral', 'exact': 'netral', 'go': 'netral', 'refund': 'netral', 'upcom': 'netral'}, 'netral'),
        ({'freak': 'negatif', 'hell': 'negatif', 'bad': 'negatif'}, 'negatif')
    ]

    # Training classifier
    classifier = NaiveBayesClassifier.train(train_data)

    # Data uji
    test_data = {'clear': 'positif', 'hope': 'positif', 'love': 'positif'}

    # Melakukan klasifikasi pada data uji
    sentiment = classifier.classify(test_data)

    print("Review:", "clear hope love")
    print("Sentimen:", sentiment)
    