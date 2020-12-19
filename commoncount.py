from collections import Counter
import pandas as pd
    
def commoncount(n):
    data=pd.read_csv('C:/Users/lenovo/Documents/FE595-HW3/all.csv')

    a=[]
    # Extract data in purpose
    for sentence in data['purpose']:
        a.append(sentence)
    b=pd.DataFrame(a)
    # Turn into one string
    b=b[0].str.cat(sep=' ')
    # Find the 10 most common words
    common=Counter(b.split()).most_common(n)
    print(common)
    

if __name__ == "__main__":
    commoncount(10)
