import urllib.request, urllib.parse,urllib.error
from bs4 import BeautifulSoup
import re
url=input('enter: url')
html=urllib.request.urlopen(url).read()
print(html)
soup=BeautifulSoup(html,'html.parser')
print(soup)
tags=soup('span')
for tag in tags:
    if tag=='span':
        print(tag.get('href'), None)
counts=list()
sum=0
for line in tags:
    words=line.decode().split()
    print(words)
    for word in words:
       word=re.findall('[0-9]+', line)
       counts.append(int(word))
       print(counts)






