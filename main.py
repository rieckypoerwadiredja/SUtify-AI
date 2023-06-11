import pandas as pd
# Utils File
from utils.menu.menu import menu, list_menu, exit_app
from utils.menu.input import getInput, getInputInt
# Main File
from utils.index import getAnalyzeResult
from utils.analyze import analyzeReview
dataset = pd.read_csv("./data/dataset.csv")

def main():
    # TODO: Berikan list menu & opening
    menu()

    # TODO: User memilih menu
    user_choice = 0
    while user_choice == 0:
        user_choice = getInputInt("Please select a menu option from 0 to 3. >> ") # ? Mau pilih menu apa user ?
        
        # Validasi Menu
        if user_choice >= 0 and user_choice <= 3:
            if(user_choice == 0):
                list_menu()
                user_choice = 0
            if(user_choice == 1):
                print("========== Write new review ==========")
                getAnalyzeResult(dataset)
                review = getInput("Tes input \n")
                # "i'm not happy the movie!"
                analyzeReview('./model/model.pickle',review)
                user_choice = 0
            if(user_choice == 2):
                print("========== Analyze review ==========")
                user_choice = 0
            if(user_choice == 3):
                exit_app()
        else:
            print("<!> Please input between 1 - 3")
            user_choice = 0
    
main()