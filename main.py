import pandas as pd
# Utils File
from utils.menu.menu import menu, list_menu, exit_app
from utils.menu.input import getInput, getInputInt
from utils.checkFileEmpty import check_file_empty
from utils.posTag import posTag
from utils.ner import ner
from utils.SinonimAntonim import sinonim_antonim
from  utils.enterToContinue import enter_to_continue
# Main File
from utils.index import getAnalyzeResult
from utils.analyze import analyzeReview

def main():
    current_review = "The new update is dissapointing"
    # TODO: Berikan list menu & opening
    menu()
    dataset = pd.read_csv("./data/dataset.csv")

    # TODO: Apakah model ada isinya ?
    is_model_empty = check_file_empty("./model/model.pickle")
    if is_model_empty == True: # Kalo belum ada isi pada file model kita run dulu dulu
        getAnalyzeResult(dataset,current_review)
    print("\n")
    
    # TODO: Berikan informasi list menu & nilai review saat ini
    list_menu()   
    print(f"Current Review: {current_review}")
    
    # TODO: User memilih menu
    user_choice = 0
    while user_choice == 0:
        user_choice = getInputInt("Please select a menu option from 0 to 3. >> ") # ? Mau pilih menu apa user ?
        
        # Validasi Menu
        if user_choice >= 0 and user_choice <= 3:
            if(user_choice == 0):
                list_menu()
                print(f"Current Review: {current_review}")
                user_choice = 0
            if(user_choice == 1):
                print("========== Write new review ==========")
                # TODO: user membarikan review yg akan dinilai nantinya --> diubah untuk analisis nanti
                user_input = "_"
                while user_input=="_":
                    review = getInput("Input your review [must be at least 3 words] \n")
                    if len(review.split(" ")) < 3:
                        print("The review must contain at least 3 words!")
                        user_input=="_"
                    else:
                        user_input=""
                    
                current_review = review
        
                print("current review:",current_review)
                user_choice = 0
            if(user_choice == 2):
                print("========== Analyze review ==========")
                print("Result of Analysis")
                print("1. Part of Speech Tags")
                # TODO: Analisis POS Tag
                list_pos_tag = posTag(current_review)
                print(list_pos_tag)
                
                # TODO: Analisis Named Entity Recognition (NER)
                ner(list_pos_tag)
                
                # TODO: Cari sinonim antonim
                print("3. Synonym(s) and Antonym(s)")
                # ? Dokumentasi: https://www.nltk.org/howto/wordnet.html
                sinonim_antonim(list_pos_tag)
                
                print("")
                # TODO: terus dapetin nilai pos atau neg pake
                print("4. Sentimen Analysis")
                analyzeReview('./model/model.pickle',current_review)
                print("")
                user_choice = 0
            if(user_choice == 3):
                exit_app()
        else:
            print("<!> Please input between 1 - 3")
            user_choice = 0
    
main()