"""
Write a program to parse 0 to 10 page of apple products from flipkart.com
and prepare an excel database showing name and price of the items.
"""


import ssl
import urllib.error
import urllib.parse
import urllib.request

import pandas as pd

from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

class ParseFlipkartProduct:
    products = []
    prices = []

    def get_input(self):
        url='https://www.flipkart.com/search?q=apple+products&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY&page='
        return url

    def get_links(self,url):
        pages=list(range(1,10))
        for page in pages:
            new_url=url+str(page)
            html = urllib.request.urlopen(new_url, context=ctx).read()
            soup = BeautifulSoup(html, 'html.parser')
            return soup

    def get_items(self,soup):
                # Retrieve all of the anchor tags
        for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
            name=a.find('div', attrs={'class':'_3wU53n'})
            price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
            self.products.append(name.text)
            self.prices.append(price.text)
            print (self.products, self.prices)

    def create_database(self,products,prices):
        df=pd.DataFrame({'product name': products, 'price': prices})
        df.to_csv('product_1_2.csv', index=False, encoding='utf-8')
        return

    def processes(self):
        input=self.get_input();
        links=self.get_links(input);
        self.get_items(links);
        self.create_database()

flipkart_database=ParseFlipkartProduct()
flipkart_database.processes()