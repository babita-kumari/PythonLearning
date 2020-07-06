"""
Write a program for a location, contact a web service and retrieve JSON for the web service and parse that data,
and retrieve the first place_id from the JSON.

"""

import urllib.request, urllib.parse, urllib.error
import json
import ssl

#http://py4e-data.dr-chuck.net/json?address=xyz&key=42
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

class FindAddress:

    def __init__(self):
        self.api_key = str(42)
        self.serviceurl = 'http://py4e-data.dr-chuck.net/json?'

    def get_input(self,api_key):
        address="bangalore"
        new_address={}
        new_address['address']=address
        new_address['key']=api_key
        return new_address

    def read_url(self,new_address,serviceurl):
        url = serviceurl + urllib.parse.urlencode(new_address)
        uh = urllib.request.urlopen(url, context=ctx)
        data = uh.read()
        data=data.decode()
        print(data)
        return data

    def load_data(self,data):
        js=json.loads(data)
        print(js)
        return js

    def find_place_id(self,js):
        place_id=[]
        for place in js["results"]:
            place_id=place[ "place_id"]
            return place_id

    def print_result(self,place_id):
        print(place_id)

    def processes(self):
        input=self.get_input(self.api_key);
        url=self.read_url(input,self.serviceurl);
        data=self.load_data(url);
        place_id=self.find_place_id(data);
        self.print_result(place_id)

place_dict=FindAddress()
place_dict.processes()







