import urllib.request, urllib.parse, urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

counts=[]

address='http://py4e-data.dr-chuck.net/comments_680101.json'
url = urllib.request.urlopen(address, context=ctx)
data = url.read()
print(data.decode())
try:
    js=json.loads(data)
except:
    js=None
print(json.dumps(js))
for i in js["comments"]:
    print(i)
    name=i["name"]
    count=i["count"]
    counts.append(int(count))
total=sum(counts)
print(total)


