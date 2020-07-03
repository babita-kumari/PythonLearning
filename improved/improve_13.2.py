import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

class ReadEmailFromHtml():

    def get_input(self):
        url = ' http://py4e-data.dr-chuck.net/known_by_Rihab.html '
        return url

    def get_links(self,url):
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        links = []
    # Retrieve all of the anchor tags
        tags = soup('a')
        for tag in tags:
            new_tag = tag.get('href')
        #print(new_tag)
            links.append(new_tag)
        return links

    def get_url(self, links):
        url_list=[]
        for i in range(0, 7):
            all_urls = links
            url = all_urls[17]
            url_list.append(url)
        return url_list

    def print_result(self,url_list):
        number=0
        for link in url_list:
            number=number+1
            print("I:",number, link)

    def processes(self):
        input=self.get_input();
        links=self.get_links(input);
        url=self.get_url(links);
        self.print_result(url)

email_dict=ReadEmailFromHtml()
email_dict.processes()





