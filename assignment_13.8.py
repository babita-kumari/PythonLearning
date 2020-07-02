import urllib.request, urllib.parse, urllib.error
import json
import ssl



api_key=str(42)
serviceurl = 'http://py4e-data.dr-chuck.net/json?'
#http://py4e-data.dr-chuck.net/json?address=xyz&key=42
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address=input('address')
new_address={}
new_address['address']=address
new_address['key']=api_key

#print(new_address)
url = serviceurl + urllib.parse.urlencode(new_address)
#print(url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
data=data.decode()
print(data)
js=json.loads(data)
#js=json.dumps(js)
print(js)
place_id=[]
for i in js["results"]:
    print(i)
    place_id=i[ "place_id"]
    print(place_id)





