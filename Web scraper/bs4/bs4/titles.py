from bs4 import BeautifulSoup
import requests
import csv

#url,req,soup
url="https://de.yahoo.com/?p=us"
req=requests.get(url)
soup=BeautifulSoup(req.text, "html.parser")
print(soup.title)

file=csv.writer(open("output5.csv","w"))
file.writerow([soup.title])





