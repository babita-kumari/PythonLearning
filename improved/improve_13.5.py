"""
Write a Python program for a URL, read the XML data from that URL using urllib and
then parse and extract the comment counts from the XML data,
compute the sum of the numbers in the file.

"""

import ssl
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

class ParseTreeFromXml:

    def get_input(self):
        address='http://py4e-data.dr-chuck.net/comments_680100.xml'
        return address

    def read_xml(self,address):
        url = urllib.request.urlopen(address, context=ctx)
        data = url.read()
        new_data=data.decode()
        print(new_data)
        return new_data

    def get_tree(self,new_data):
        trees = ET.fromstring(new_data)
        content=trees.findall('comments/comment')
        return content

    def find_name(self,content):
        name_list=[]
        for item in content:
            print(item)
            name=item.find('name').text
            name_list.append(name)
        return name_list

    def find_count(self,content):
        count_list=[]
        for item in content:
            count=item.find('count').text
            count_new=int(count)
            count_list.append(count_new)
        return count_list

    def print_result(self,name_list,count_list):
        print(name_list,count_list)

    def sum_count_list(self,count_list):
        total=sum(count_list)
        print(total)

    def processes(self):
        input=self.get_input();
        xml=self.read_xml(input);
        tree=self.get_tree(xml);
        name=self.find_name(tree);
        count=self.find_count(tree);
        self.print_result(name,count);
        self.sum_count_list(count)

xml_data=ParseTreeFromXml()
xml_data.processes()









