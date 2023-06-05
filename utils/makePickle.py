import pickle
import os

def dirValidation(dir):
    if os.path.exists(dir): # File nya udh ada belum ?
        return True
    else:
        os.makedirs(dir) # dibuat dulu direktorinya, baru keluar
        return True
    
def makePickel(dir,classifier,folder):
    dirValidation(folder)
    with open(dir, 'wb') as file:
        pickle.dump(classifier, file)
    
        