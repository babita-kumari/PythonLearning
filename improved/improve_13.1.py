

import ssl
from urllib.request import urlopen

from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

class ParseHtmlFile:

    def get_input(self):
        url = " http://py4e-data.dr-chuck.net/comments_680098.html"
        html = urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html,"html.parser")
        return soup

    def get_data(self,soup):
        tag_list=[]
        tags=soup('span')
        for tag in tags:
            tag = tag.contents[0]
            tag_new = str(tag)
            int_tag = int(tag_new)
            tag_list.append(int_tag)
        return tag_list

    def get_sum(self,tag_list):
        sum=0
        for number in tag_list:
            sum=sum+number
        return sum

    def get_count(self,tag_list):
        count=len(tag_list)
        return count

    def print_result(self,sum,count):
        print(sum,count)

    def processes(self):
        input=self.get_input();
        data=self.get_data(input);
        sum=self.get_sum(data);
        count=self.get_count(data);
        self.print_result(sum,count)

data_bank=ParseHtmlFile()
data_bank.processes()





