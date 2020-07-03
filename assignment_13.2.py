import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = ' http://py4e-data.dr-chuck.net/known_by_Rihab.html '

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


for i in range(0, 7):
    all_urls = getlinks(url)
    url = all_urls[17]
    print("I: ", i, url)



"""
    
"""
