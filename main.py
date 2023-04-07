# NLTK
from nltk import word_tokenize, sent_tokenize
from nltk.probability import FreqDist

# Utils
from utils.cleaners import indexCleaner
from utils.plot import plot
from utils.analyze import analyze

text = "Great music service, the audio is high quality and the app is easy to use. Also very quick and friendly support."

def cleanWord(text):
    # Get Word from text
    word = word_tokenize(text)
    # Clean Word
    cleanWord = indexCleaner(word)
    # Show Plot
    fd = FreqDist(cleanWord)
    plot(30,fd)
    # Analyze
    analyzeResult = analyze(cleanWord)
    
    for res in analyzeResult:
        print(res['text'])
        print(res['score'])
        
        
    # Tampilkan hasli analisis

    
cleanWord(text)

def cleanSent(text):
    # get sent from text
    sent = sent_tokenize(text)
    # Clean Sent
    cleanSent = indexCleaner(sent)
    # Show Plot
    fd = FreqDist(cleanSent)
    plot(30,fd)
    # Analyze
    analyzeResult = analyze(cleanSent)
    
    for res in analyzeResult:        
        print(res['text'])
        print(res['score'])
    # Tampilkan hasli analisis

cleanSent(text)