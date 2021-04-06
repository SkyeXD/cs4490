import urllib
from xml.dom import minidom
import xml.dom.minidom
import pandas
import numpy
import xml.etree.ElementTree as ET
import mysql.connector
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="Gfriend12+",
#   database="yxie273cs4490")
# print(mydb)
# mycursor = mydb.cursor()
# mycursor.execute("SHOW TABLES")

# for x in mycursor:
#   print(x)
tree = ET.parse('authors.xml')
root = tree.getroot()
lenTree = len(root)
authorList = [-1]*10*lenTree
authorLists = [[-1]*20]*10* lenTree
arrayIndex = 0
authorid = 0
pid = []*lenTree
for n in range(lenTree):
    myroot = root[n]
    for index, i in enumerate (myroot):

        # print(index)

        if i.tag == "author":
            for index1, m in enumerate(i):
                if(m.tag == 'name'):

                    # q = 0
                    # print(index1, m, n,q)
                    authorList[arrayIndex] = m.text.split(' ')
                    # authorLists[n][q]=authorid
                    # print(authorid)
                    # print(authorList[arrayIndex][-1], authorList[arrayIndex][0])
                    sqlauthor = "INSERT INTO authors (id,lastname,firstname) VALUES (%s, %s, %s)"

                    valauthor = (authorid, authorList[arrayIndex][-1], authorList[arrayIndex][0])

                    # mycursor.execute(sqlauthor, valauthor)
                    # mydb.commit()



                    authorid+=1
                    # q+=1
                    # print(authorList[arrayIndex][-1], authorList[arrayIndex][0])

                    arrayIndex+=1

            authorList[arrayIndex] = n

            arrayIndex += 1

    # print(myroot[0].text, myroot[3].text)
    sqlpaper = "INSERT INTO papers (id, title) VALUES (%s, %s)"
    val = (myroot[0].text, myroot[3].text)
    pid = []
    # mycursor.execute(sqlpaper, val)
    # mydb.commit()
    # print(mycursor.rowcount, "record inserted.")
print(authorList)

# print(authorLists)
sqlsort = "SELECT * FROM authors ORDER BY id"
# mycursor.execute(sqlsort)
# myresult = mycursor.fetchall()
numNotNegOne = 0
for x in authorList:
  if x != -1:
      numNotNegOne +=1
print(numNotNegOne)
index = 0
for t in range(numNotNegOne):
    if type(authorList[t]) == int:
        print("1")
        print(root[authorList[t]][0].text)
        sqlmatch = "INSERT INTO matching (authorId, paperId) VALUES (%s, %s)"
        valmatch = (index, root[authorList[t]][0].text)
        # mycursor.execute(sqlmatch, valmatch)
        # mydb.commit()
        index+=1




