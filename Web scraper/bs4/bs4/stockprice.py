import requests
from bs4 import BeautifulSoup

def parseprice():
    req=requests.get('https://finance.yahoo.com/quote/CL%3DF?p=CL%3DF')
    soup=BeautifulSoup(req.text,'lxml')
    price=soup.find('div',{'class':'D(ib) Mend(20px)'}).findAll('span')
    return price[0].text 

# while True:
print('th current price: '+str(parseprice()))    