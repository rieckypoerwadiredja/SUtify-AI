def classify(analyzeResult):
    negative_words = []
    neutral_words = []
    positive_words = []
    
    for res in analyzeResult:
        # print(res['text'],res['negative_score'],res['neutral_score'],res['positive_score'])
        if res['negative_score'] == 1.0:
            negative_words.append({
                "word": res['text'],
                "negative_score": res['negative_score']
            })
        if res['neutral_score'] == 1.0:
            neutral_words.append({
                "word": res['text'],
                "neutral_score": res['neutral_score']
            })
        if res['positive_score'] == 1.0:
            positive_words.append({
                "word": res['text'],
                "positive_score": res['positive_score']
            })
    return negative_words, neutral_words, positive_words
