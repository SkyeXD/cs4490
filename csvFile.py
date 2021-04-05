import pandas as pd
df = pd.read_csv("/Users/skye/Documents/2021 winter uwo /cs4490/4490/pnrn.csv")
# print(df.iloc[:,5])
raceList=[]
i = 0
for race in df.iloc[:,5]:
    if(df.iloc[i,4] !=" "):

        if(race == "HL+W" or race =="HL+B" or race =="HL+M" or race == "HL+O"):
            raceList.append('hispanic')
        elif(race == "NL+W" or race == "NL+O" or race == "NL+M" or race == "NL+I" ):
            raceList.append('white')
        elif (race == "NL+A"):
            raceList.append('api')
        elif (race == "NL+B"):
            raceList.append('black')
        else:
            raceList.append(' ')
            print(i, race)
    else:
        raceList.append(' ')
        print(i, race)
    i += 1

print(raceList)
df['predRace'] = raceList
print(df)
df.to_csv("/Users/skye/Documents/2021 winter uwo /cs4490/4490/pnrn2.csv")