# Matplotlib
import matplotlib.pyplot as plt

def plot(y=None,data = False):
    if data == False:
        print("<!> Error plot: Pilih komponent yang ingin divisualisasi")
        return False
    if y == None:
        print("<!> Error plot: Harus memasukan nilai y")
        return False
        
    data.plot(y)
    plt.show()