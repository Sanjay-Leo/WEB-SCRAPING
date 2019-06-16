from bs4 import BeautifulSoup
import requests

price = input("enter budget :")
res = requests.get("https://www.flipkart.com/search?q=smartphone%20under%20" + price)
soup = BeautifulSoup(res.text, "lxml")

# y = soup.find_all('div', class_="_3BTv9X")

x = soup.find_all("div", class_="col col-7-12")

phone = []
for i in x:
    phone.append(i.find_all("div", class_="_3wU53n"))
    phone.append(i.find_all("li"))
    phone.append(i.find_all("img"))

# store = []
# for i in y:
#   store.append(i.find_all('img',class_="_1Nyybr  _30XEf0")

for each_phone in phone:
    print(each_phone[0].text)
