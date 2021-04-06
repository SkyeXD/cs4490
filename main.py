# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# import urllib3
# url = 'https://arxiv.org/list/cs.DB/2012?skip=0&show=500/query?search_query=au'
url = 'http://export.arxiv.org/api/query?search_query=cat:cs.DB&start=0&max_results=10000'
# url1 = 'https://www.census.gov/data/developers/data-sets/surnames.html'


import requests

r = requests.get(url)
f = open("authorFinal.xml", "w")
f.write(r.text)
f.close()



