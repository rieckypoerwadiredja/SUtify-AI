# Utils File
from utils.readFile import readCsv
from utils.menu.menu import menu, list_menu, exit_app
from utils.menu.input import getInput, getInputInt
# Main File
from utils.index import getWord

text = readCsv(['Review'],'./data/dataset.csv') 
text = text.tolist()

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
                user_choice = getInputInt("Please select a menu option from 0 to 3 >> ")
            if(user_choice == 1):
                print("========== Write new review ==========")
                getWord(text)   
                user_choice = getInputInt("Please select a menu option from 0 to 3 >> ")
            if(user_choice == 2):
                print("2. Analyze review")
                user_choice = getInputInt("Please select a menu option from 0 to 3 >> ")
            if(user_choice == 3):
                exit_app()
        else:
            print("<!> Please input between 1 - 3")
            user_choice = 0
    
main()