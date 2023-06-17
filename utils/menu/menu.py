import keyboard
from utils.checkFileExists import check_file_exists
from utils.enterToContinue import enter_to_continue
current_review = "The new update is dissapointing"
dataset_name = "dataset.csv"

        
def list_menu():
    print("0. List menu")
    print("1. Write new review")
    print("2. Analyze review")
    print("3. Exit")
    
def menu():
    print("welcome to the SUtify Review Analyzer")
    print("👋👋 =========== 👋👋 =========== 👋👋")
    print("\n")
    print(f"Current Review: {current_review}")
    print("<!> Please make sure to prepare a dataset in CSV format inside the 'data' folder named 'dataset'.")
    # ? Deley until enter
    enter_to_continue("Is the file already available? (Press 'enter' to continue)")
    
    # TODO: Validasi apakah file dataset sudah ada ?
    is_dataset_exists = check_file_exists(dataset_name,"data")
    if is_dataset_exists == False:
        exit()
    
    print("\n")    
    # TODO: Apakah model sudah ada ?
    print("<!> Please make sure to prepare a model in pickle format inside the 'data' folder named 'model.pickle'.")
    is_model_exists = check_file_exists("model.pickle","model")
    if is_model_exists == False: # Kalo belum ada model kita buat dulu
        with open("./model/model.pickle", 'wb') as file:
            pass

def exit_app():
    print("Exit SUtify App \n Bay-Bay!👋👋👋")
    exit()
    
    
        