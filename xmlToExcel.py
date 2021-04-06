import urllib
from xml.dom import minidom
import xml.dom.minidom
import pandas as pd
import numpy as np
import xml.etree.ElementTree as ET


au_paper = []
tree = ET.parse('authors.xml')
root = tree.getroot()
lenTree = len(root)
authorList = [-1]*10*lenTree
authorLists = [[-1]*20]*10* lenTree
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
print(authorList)
for n in range(lenTree):
    myroot = root[n]
    for index, i in enumerate (myroot):

        # print(index)
        if i.tag == "id":
            paperId=i.text

        if i.tag == "author":
            for index1, m in enumerate(i):
                if(m.tag == 'name' ):
                    # if(m.text.split(' ') not in authorList):
                    authorList[arrayIndex] = m.text.split(' ')
                    print(authorList)



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


# print(authorLists)
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


print(au_paper)
author = {'fname':authorFirstName1,'lname':authorLastName1,'paperId': au_paper}
# print(author)
matching = {'aid':amatching,'pid':pmatching}
paperdf = pd.DataFrame(data = paper)
authordf = pd.DataFrame(data = author)
matchdf = pd.DataFrame(data = matching)
# print(authordf)
paperdf.to_csv("paper1.csv")
authordf.to_csv("author2.csv")
matchdf.to_csv("matching1.csv")
paperdf.to_excel("paper1.xlsx")
authordf.to_excel("author1.xlsx")
matchdf.to_excel("matching1.xlsx")
