import pandas as pd

def readCsv(usecols = [], data = None):
    if data == None:
        print("<!> Error readCsv: masukan root data!")
    # usecols untuk kolom mana aja yang dipake
    # index_col untuk tidak memakai row number  
    df = pd.read_csv(data, usecols=usecols, index_col=0) 
    # print(df.head(5).index)
    return df.index