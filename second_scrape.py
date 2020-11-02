import requests
import bs4
import lxml

res = requests.get("https://en.wikipedia.org/wiki/Grace_Hopper")

soup = bs4.BeautifulSoup(res.text,"lxml")

items = soup.select('.toctext')

for item in items:
    print(item.text)