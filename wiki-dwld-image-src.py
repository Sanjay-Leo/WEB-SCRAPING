from bs4 import BeautifulSoup
import requests

res = requests.get("https://en.wikipedia.org/wiki/lilium")
soup = BeautifulSoup(res.text, 'lxml')

img_tag = soup.find_all('img')

links = []
for i in img_tag:
    links.append('http:'+ i['src'])
    
for i in links:
    print(i)

""" half written complete it"""