from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = " http://py4e-data.dr-chuck.net/comments_680098.html"
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
sum=0
count=0
tag_list=list()
tags = soup('span')
for tag in tags:
    tag=tag.contents[0]
    tag_new=str(tag)
    count=count+1
    int_tag=int(tag_new)
    sum=sum+int_tag
print(sum,count)

#for i in tag_list:
    #sum=sum+i
    #count=count+1
#print(sum,count)

