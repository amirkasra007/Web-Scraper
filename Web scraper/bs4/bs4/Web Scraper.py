from bs4 import BeautifulSoup
import requests
import csv

#url,req,soup
url="https://de.yahoo.com/?p=us"
req=requests.get(url)
soup=BeautifulSoup(req.text, "html.parser")
print(soup.title)

file=csv.writer(open("output2.csv","w"))
file.writerow([soup.title])

out=soup.find_all('a')
out1=[]
for link in soup.find_all('a'):
    print(link.get('href'))

file=csv.writer(open("output4.csv","w"))
file.writerow([soup.find_all('a')])  


print(soup.find_all('p'))

print(soup.find_all('h6'))
print(soup.find_all('h1'))
print(soup.find_all('h2'))

print(soup.find_all('h3'))
print(soup.find_all('h4'))
print(soup.find_all('h5'))


print(soup.find_all('strong'))
print(soup.find_all('div'))

print(soup.find_all('style'))
print(soup.find_all('img'))

print(soup.find_all('b'))
print(soup.prettify())

