"""
Write a program that will use urllib to read the HTML from the data files, extract the href= values from the anchor tags,
 scan for a tag that is in a particular position relative to the first name in the list,
follow that link and repeat the process a number of times and report the last name you find.
Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times.
The answer is the last name that you retrieve.
"""

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE



def get_links(url):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    # Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        new_tag = tag.get('href')
        links.append(new_tag)
    return links

class ReadEmailFromHtml():
    url = ' http://py4e-data.dr-chuck.net/known_by_Rihab.html '

    def get_url(self):
        url_list=[]
        for i in range(0, 7):
            all_urls=get_links(self.url)
            new_url = all_urls[17]
            url_list.append(new_url)
            self.url=new_url
        return url_list

    def print_result(self,url_list):
        number=0
        for link in url_list:
            number=number+1
            print("I:",number, link)

    def processes(self):
        links=self.get_url();
        self.print_result(links)

email_dict=ReadEmailFromHtml()
email_dict.processes()





