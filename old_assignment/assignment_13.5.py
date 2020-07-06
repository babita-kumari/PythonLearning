

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
address='http://py4e-data.dr-chuck.net/comments_680100.xml'


names=list()
counts=list()
url = urllib.request.urlopen(address, context=ctx)
data = url.read()
print(data.decode())
tree = ET.fromstring(data)
lst=tree.findall('comments/comment')
print('comments_count', len(lst))
for item in lst:
    name=item.find('name').text
    count=item.find('count').text
    count_new=int(count)
    names.append(name)
    counts.append(count_new)
print(names,counts)
total=sum(counts)
print(total)







