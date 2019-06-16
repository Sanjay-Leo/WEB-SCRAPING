from bs4 import BeautifulSoup
import requests
res = requests.get(
    "https://en.wikipedia.org/wiki/List_of_cities_in_India_by_population"
)
soup = BeautifulSoup(res.text, "lxml")

soup.title.text

table = soup.findAll("table", attrs={"class": "wikitable sortable"})
soup.p

tb = []
for t in table:
    x = t.findAll("tbody")
    tb.append(x)
tr = []
for trow in tb:
    tr.append(trow[0].findAll("tr"))

cities = []

for t_r in tr:
    for i in range(1, len(t_r)):
        cities.append(t_r[i].find("a").text)

tr[1][13].find("a").text
print(cities)
