"""
Scraping Numbers from HTML using BeautifulSoup
Write a program to use urllib to read the HTML from the data files and parse the data,
extracting numbers and compute the sum of the numbers in the file.
"""

import urllib.request, urllib.parse,urllib.error
from bs4 import BeautifulSoup
import re

class ParseFromHtml:

    def get_input(self):
        url=" http://py4e-data.dr-chuck.net/comments_680098.html"
        html=urllib.request.urlopen(url).read()
        soup=BeautifulSoup(html,'html.parser')
        return soup

    def read_tag(self, soup):
        tag_list=[]
        tags=soup('span')
        for tag in tags:
            if tag=='span':
                tag=tag.get('href')
            tag_list.append(tag)
        return tag_list

    def decode_tags(self,tag_list):
        word_list=[]
        for line in tag_list:
            print(line)
            words=line.decode().split()
            word=words[1]
            word_list.append(word)
        print(word_list)
        return word_list


    def store_number(self,word_list):
        print("Inside store number method")
        number_list = []
        for word in word_list:
            number=re.findall(r'[0-9]+',word)
            number_list.append(int(number[0]))
        return number_list

    def print_result(self, number_list):
        total=sum(number_list)
        print("total sum of numbers is: ", total)


    def processes(self):
        input=self.get_input();
        tag=self.read_tag(input);
        decoded_tag=self.decode_tags(tag);
        number=self.store_number(decoded_tag);
        self.print_result(number)

tags=ParseFromHtml()
tags.processes()








