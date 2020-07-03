import urllib.request, urllib.parse, urllib.error
import json
import ssl

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
        #js=json.dumps(js)
        return js

    def find_name(self,js):
        names=[]
        for element in js["comments"]:
            name=element["name"]
            names.append(name)
        print(names)
        return names

    def find_count(self,js):
        counts=[]
        for element in js["comments"]:
            count=element["count"]
            count_new=int(count)
            counts.append(count_new)
        return counts

    def print_sum(self,counts):
        total=0
        for number in counts:
            total+=sum(counts)
        print(total)

    def processes(self):
        input=self.get_input();
        file=self.open_file(input);
        data=self.load_data(file);
        content=self.find_name(data);
        count=self.find_count(data);
        self.print_sum(count)

data_list=ProcessesJson()
data_list.processes()




