from nltk import ne_chunk
from utils.makePlot import make_plot
from utils.enterToContinue import enter_to_continue

def ner(list_pos_tag):  
    # ? Dokumentasi: https://tedboy.github.io/nlps/generated/generated/nltk.ne_chunk.html
    ner = ne_chunk(list_pos_tag) # Buat dulu hubungan antar akatanya nanti
                
    enter_to_continue()
    
    make_plot(ner)