import os

def check_file_exists(file_name,folder_name):
    project_dir = os.getcwd()  # Mendapatkan direktori projek saat ini
    data_dir = os.path.join(project_dir, folder_name)  # Beralih ke direktori "./data" di dalam direktori projek
    file_path = os.path.join(data_dir, file_name)  # Membangun path lengkap berdasarkan direktori "./data" dan nama file
    if os.path.exists(file_path):
        print(file_path)
        print(f"{file_name} have been found")
        return True
    else:
        print(f"file not found\nMake sure the {file_name} file already exists in the {file_path} directory")
        return False