# NLTK
from nltk import word_tokenize, sent_tokenize
from nltk.probability import FreqDist

# Utils
from utils.cleaners import indexCleaner
from utils.plot import plot
from utils.analyze import analyze
from utils.readFile import readCsv

text = readCsv(['Review'],'./data/dataset.csv') 
text = text.tolist()

def cleanWord(text):
    # Get Word from text
    words = []
    for sent in text:
        word = word_tokenize(sent)
        words.append(word)
        
    #  Merubah array dalam array ke 1 array
    flattened_words = []
    for wordArray in words:
        for word in wordArray:
            flattened_words.append(word)
    
    # Clean Word
    cleanWord = indexCleaner(flattened_words)
    # Show Plot
    fd = FreqDist(cleanWord)
    plot(50,fd)
    # Analyze
    analyzeResult = analyze(cleanWord)
    
    for res in analyzeResult:
        print(res['text'])
        print(res['score'])
        
        
    # Tampilkan hasil analisis plot

    
cleanWord(text)

def cleanSent(text):
    sents = []
    # get sent from text
    for sent in text:
        sent = sent_tokenize(sent)
        sents.append(sent)
    print(sents)
    #  Merubah array dalam array ke 1 array
    flattened_sents = []
    for sendArray in sents:
        for sent in sendArray:
            flattened_sents.append(sent)
            
    # Clean Sent
    cleanSent = indexCleaner(flattened_sents)
    # Show Plot
    fd = FreqDist(cleanSent)
    plot(30,fd)
    # Analyze
    analyzeResult = analyze(cleanSent)
    
    for res in analyzeResult:        
        print(res['text'])
        print(res['score'])
        
    # Tampilkan hasil analisis plot

cleanSent(text)