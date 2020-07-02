
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import pandas as pd
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

products = []
prices=[]
pages=list(range(1,10))
url = 'https://www.flipkart.com/search?q=apple+products&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY&page='
for page in pages:
    new_url=url+str(page)
    html = urllib.request.urlopen(new_url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
        # Retrieve all of the anchor tags
    for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
        name=a.find('div', attrs={'class':'_3wU53n'})
        price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
        products.append(name.text)
        prices.append(price.text)
print(products,prices)
df=pd.DataFrame({'product name': products, 'price': prices})
df.to_csv('product_1_2.csv', index=False, encoding='utf-8')