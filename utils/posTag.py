 # TODO: Nilai dari current_review --> POS (nnt dpt tiap kata itu apasih maksudnya)
# ? Dokumentasi: https://www.nltk.org/api/nltk.tag.pos_tag.html
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
     
def posTag(sent):
    get_words_current_review = word_tokenize(sent)
    pos_tag_current_review = pos_tag(get_words_current_review)
    
    for index, posTag in enumerate(pos_tag_current_review):
        print(f"{index}) {posTag[0]}, {posTag[1]}")
        
    return pos_tag_current_review