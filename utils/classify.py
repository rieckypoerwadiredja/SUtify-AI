def classify(analyzeResult):
    negatives = []
    neutrals = []
    positives = []
    
    for res in analyzeResult:
        # print(res['text'],res['negative_score'],res['neutral_score'],res['positive_score'])
        if res['negative_score'] == 1.0:
            negatives.append({
                "text": res['text'],
                "negative_score": res['negative_score']
            })
        if res['neutral_score'] == 1.0:
            neutrals.append({
                "text": res['text'],
                "neutral_score": res['neutral_score']
            })
        if res['positive_score'] == 1.0:
            positives.append({
                "text": res['text'],
                "positive_score": res['positive_score']
            })
    return negatives, neutrals, positives

def classify_sentence(analyzeResult):
    negatives = []
    neutrals = []
    positives = []
    for res in analyzeResult:
        # print(res['compound']) 
        if res['score']['compound'] >= 0.05:
            positives.append({
                "text": res['text'],
                "positive_score": res['positive_score']
            })
        elif res['score']['compound'] <= -0.05:
            negatives.append({
                "text": res['text'],
                "negative_score": res['negative_score']
            })
        else:
            neutrals.append({
                "text": res['text'],
                "neutral_score": res['neutral_score']
            })
    return negatives, neutrals,positives

