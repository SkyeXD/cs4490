
import urllib
from xml.dom import minidom
import xml.dom.minidom
import pandas as pd
import numpy as np
import xml.etree.ElementTree as ET


au_paper = []
tree = ET.parse('authorFinal.xml')
root = tree.getroot()
lenTree = len(root)
authorList = [-1]*10*lenTree
authorLists = [[-1]*20]*10* lenTree
authorList1 = []
authorLists1 = []
arrayIndex = 0
p=0
authorid = 0
pid = [' ']*lenTree
ptitle = [' ']*lenTree
aid = [' ']*lenTree*10
paperId = None


authorLastName = [' ']*lenTree*10
authorFirstName = [' ']*lenTree*10
authorLastName1 = []
authorFirstName1 = []

for n in range(lenTree):
    myroot = root[n]
    for index, i in enumerate (myroot):
        tempTime = myroot[2].text.split("-")[0]

        # print(index)
        if i.tag == "id":
            paperId=i.text

        if i.tag == "author":
            for index1, m in enumerate(i):
                if(m.tag == 'name' ):
                    # if(m.text.split(' ') not in authorList):
                    authorList[arrayIndex] = m.text.split(' ')
                    tempLast = m.text.split(' ')[-1]
                    tempFirst = m.text.split(' ')[0]
                    temp = []
                    temp += [tempFirst,tempLast,tempTime,paperId]
                    # temp = m.text.split(' ')
                    # temp += [tempTime]
                    authorList1.append(temp)



                    sqlauthor = "INSERT INTO authors (id,lastname,firstname) VALUES (%s, %s, %s)"


                    aid[p] = authorid
                    authorFirstName[p] = authorList[arrayIndex][0]
                    authorLastName[p] = authorList[arrayIndex][-1]
                    authorFirstName1.append(authorList[arrayIndex][0])
                    authorLastName1.append(authorList[arrayIndex][-1])
                    au_paper.append(paperId)

                # print(paperId,authorFirstName[p],authorLastName[p])




                    authorid+=1


                    arrayIndex+=1
                    p+=1

            authorList[arrayIndex] = n

            arrayIndex += 1

    # print(myroot[0].text, myroot[3].text)

    val = (myroot[0].text, myroot[3].text)
    pid[n] = myroot[0].text
    ptitle[n] = myroot[3].text

print(authorList1)
# print(authorLists)
finalLast = []
finalFirst = []
finalYear = []
finalId = []
for i in authorList1:
    print(i[1])
    finalFirst.append(i[0])
    finalLast.append(i[1])
    finalYear.append(i[2])
    finalId.append(i[3])
sqlsort = "SELECT * FROM authors ORDER BY id"
numNotNegOne = 0
for x in authorList:
  if x != -1:
      numNotNegOne +=1

index = 0
amatching = [' ']*numNotNegOne
pmatching = [' ']*numNotNegOne
for t in range(numNotNegOne):
    if type(authorList[t]) == int:
        # print("1")
        # print(root[authorList[t]][0].text)
        sqlmatch = "INSERT INTO matching (authorId, paperId) VALUES (%s, %s)"
        valmatch = (index, root[authorList[t]][0].text)
        amatching[t] = index
        pmatching[t] = root[authorList[t]][0].text

        index+=1
# print(authorFirstName)
# firstName = list(dict.fromkeys(authorFirstName))
# print(firstName)
# lastName = list(dict.fromkeys(authorLastName))
# print(lastName)

paper = {'id':pid,'title':ptitle}
print(len(finalFirst),len(finalLast),len(finalYear),len(finalId))


author = {'fname':finalFirst,'lname':finalLast,'year': finalYear,'paperId': finalId}

authordf = pd.DataFrame(data = author)

print(authordf)
authordf.to_csv("authorFinal.csv")


