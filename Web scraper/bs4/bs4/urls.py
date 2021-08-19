from bs4 import BeautifulSoup
import requests
import csv

#url,req,soup
url="https://de.yahoo.com/?p=us"
req=requests.get(url)
soup=BeautifulSoup(req.text, "html.parser")

out=soup.find_all('a')
out1=[]
for link in soup.find_all('a'):
    print(link.get('href'))

file=csv.writer(open("output4.csv","w"))
file.writerow([soup.find_all('a')])    

