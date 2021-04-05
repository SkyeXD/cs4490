import pandas as pd
import numpy as np
authors = {}
authordf = pd.read_csv("bt3.csv")

for i in range(authordf.shape[0]):
    coAuthor = []
    temp = []
    akey = authordf.iloc[i,1]+" "+authordf.iloc[i,2]
    for j in range(authordf.shape[0]):
        if(authordf.iloc[j,3] == authordf.iloc[i,3]):
            if(authordf.iloc[j,1]+" "+authordf.iloc[j,2] != akey):
                coAuthor.append(authordf.iloc[j,1]+" "+authordf.iloc[j,2])

    authors[akey] = coAuthor

print(authors)