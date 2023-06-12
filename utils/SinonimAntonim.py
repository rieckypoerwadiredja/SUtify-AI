from nltk.corpus import wordnet as wn

def sinonim_antonim(list_pos_tag = False):
    if list_pos_tag == False:
        print("<!> list_pos_tag must avalaible")
        return
    # ? Dokumentasi: https://www.nltk.org/howto/wordnet.html
    for posTagTup in enumerate(list_pos_tag):  
        print("")  
        print("Word:", posTagTup[1][0])
        print("")
                                
        sysnonym_list =[]
        antonym_list =[]

        # TODO: Sinonim
        sinonim = wn.synsets(posTagTup[1][0])
        print("Sysnonym(s)") 
        for sin in sinonim:
            for lemma in sin.lemmas():
                sysnonym_list.append(lemma.name()) # Mendapat nilai word dari sinonim
                # TODO: Antonim
                for antonim in lemma.antonyms():
                    antonym_list.append(antonim.name()) # Mendapat nilai word dari antonim
                                            
        if len(sysnonym_list) < 1:
            print(f"{posTagTup[1][0]} has no synonym")
        else: 
            print(sysnonym_list)
                                    
        print("")
        print("Word:", posTagTup[1][0])
        print("")
        print("Antonym(s)") 
                                
        if len(antonym_list) < 1:
            print(f"{posTagTup[1][0]} has no synonym")
        else: 
            print(antonym_list)
                