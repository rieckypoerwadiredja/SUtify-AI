import keyboard
import os
import time

current_review = "The new update is dissapointing"
dataset_name = "dataset.csv"

def check_file_exists(file_name):
    project_dir = os.getcwd()  # Mendapatkan direktori projek saat ini
    data_dir = os.path.join(project_dir, "data")  # Beralih ke direktori "./data" di dalam direktori projek
    file_path = os.path.join(data_dir, file_name)  # Membangun path lengkap berdasarkan direktori "./data" dan nama file
    if os.path.exists(file_path):
        print("files have been found")
        time.sleep(2)
        print("\n")
    else:
        print("file not found\nMake sure the dataset.csv file already exists in the ./data/dataset.csv directory")
        exit()
        
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
    print("Is the file already available? (Press 'enter' to continue)")
    keyboard.wait("enter")
    print("\n")
    # TODO: Validasi apakah file sudah ada ?
    check_file_exists(dataset_name)
    # TODO: Berikan list menu
    list_menu()

def exit_app():
    print("Exit SUtify App \n Bay-Bay!👋👋👋")
    exit()
    
    
        