# these should be the only imports you need

import requests
from bs4 import BeautifulSoup

# write your code here
# usage should be python3 part3.py

print("Michigan Daily -- MOST READ")
url = "http://www.michigandaily.com"
html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")

# dictionary to hold data
articleInfo = {}

# get article title and the link to the article
for link in soup.find_all(class_="pane-mostread"):
    for a in link.find_all("a", href=True):
        articleInfo[a.contents[0]] = a["href"]

# use the link to the article to get author and overwrite the link with the author
for article in articleInfo:
    soup = BeautifulSoup(requests.get(url + articleInfo[article]).text, "html.parser")
    for link in soup.find_all(class_="link"):
        for a in link.find_all("a"):
            articleInfo[article] = a.contents[0]

# print most read articles
for articleTitle, author in articleInfo.items():
    print(articleTitle)
    print("  by", author)