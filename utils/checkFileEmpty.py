import os
def check_file_empty(file_dir):
    return os.stat(file_dir).st_size == 0