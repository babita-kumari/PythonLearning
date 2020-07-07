"""
Write a Python program for a URL, read the json data from that URL using urllib and
then parse and extract the comment counts from the json data,
compute the sum of the numbers in the file.
"""

import json
import ssl
import urllib.error
import urllib.parse
import urllib.request

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

class ProcessesJson:

    def get_input(self):
        address = 'http://py4e-data.dr-chuck.net/comments_680101.json'
        return address

    def open_file(self,address):
        url = urllib.request.urlopen(address, context=ctx)
        data = url.read()
        data.decode()
        return data

    def load_data(self,data):
        try:
            js=json.loads(data)
        except:
            js=None
        return js

    def find_name_count(self,js):
        names=[]
        counts=[]
        for element in js["comments"]:
            name=element["name"]
            count=element["count"]
            names.append(name)
            counts.append(int(count))
        print(names,counts)
        return counts

    def print_sum(self,counts):
        total=0
        for number in counts:
            total=sum(counts)
        print(total)

    def processes(self):
        input=self.get_input();
        file=self.open_file(input);
        data=self.load_data(file);
        content=self.find_name_count(data);
        self.print_sum(content)

data_list=ProcessesJson()
data_list.processes()




