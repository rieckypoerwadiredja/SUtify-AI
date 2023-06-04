from nltk.sentiment import SentimentIntensityAnalyzer

# {'neg': 0.0, 'neu': 0.394, 'pos': 0.606, 'compound': 0.7322}
# neu: Skor sentimen netral dari kalimat. Dalam hal ini, nilai 0.674 menunjukkan bahwa sebagian besar kalimat cenderung netral.
# pos: Skor sentimen positif dari kalimat. Dalam hal ini, nilai 0.326 menunjukkan bahwa terdapat sedikit sentimen positif pada kalimat tersebut.
# compound: Skor sentimen keseluruhan dari kalimat, yang merupakan gabungan dari skor sentimen positif, negatif, dan netral. Skor sentimen keseluruhan dinyatakan dalam rentang nilai -1 hingga 1, di mana nilai -1 menunjukkan sentimen yang sangat negatif, 0 menunjukkan sentimen netral, dan 1 menunjukkan sentimen yang sangat positif. Dalam hal ini, nilai 0.4404 menunjukkan bahwa kalimat tersebut memiliki sentimen yang cukup positif.

def analyze(data=[]):
    if len(data) < 1:
        print("<!> Error 'wordList' data tidak valid")
        
    sia = SentimentIntensityAnalyzer()
    allScore = []
    for text in data:
        score = sia.polarity_scores(text)
        
        # Mendapatkan skor positif, negatif, dan netral
        positive_score = score['pos']
        negative_score = score['neg']
        neutral_score = score['neu']

        objectScore = {
            "text": text,
            "score": score,
            "neutral_score": neutral_score,
            "negative_score": negative_score,
            "positive_score": positive_score
        }
        allScore.append(objectScore)
    return allScore

from nltk.sentiment import SentimentIntensityAnalyzer

def analyze_sentence(data):
    if not data:
        print("<!> Error: Data kosong.")
        return None
        
    sid = SentimentIntensityAnalyzer()
    all_scores = []
    
    for text in data:
        score = sid.polarity_scores(text)
        
        # Mendapatkan skor positif, negatif, dan netral
        positive_score = score['pos']
        negative_score = score['neg']
        neutral_score = score['neu']

        object_score = {
            "text": text,
            "score": score,
            "neutral_score": neutral_score,
            "negative_score": negative_score,
            "positive_score": positive_score
        }
        
        all_scores.append(object_score)
    
    return all_scores