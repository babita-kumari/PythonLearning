import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter - ')

def getlinks(url):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    links = []

    # Retrieve all of the anchor tags

    tags = soup('a')
    for tag in tags:
        new_tag = tag.get('href')
        #print(new_tag)
        links.append(new_tag)
    return links

def getnames(url):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    names=[]

    # Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        tag = tag.contents[0]
        tag_new = str(tag)
        names.append(tag_new)
    return names

for i in range(0, 7):
    all_urls = getlinks(url)
    all_names=getnames(url)
    url = all_urls[17]
    name=all_names[17]
    print("I: ", i, url, name)