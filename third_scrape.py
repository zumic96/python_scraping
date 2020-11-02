import requests
import bs4
import lxml

res = requests.get("https://hr.wikipedia.org/wiki/Deep_Blue")

soup = bs4.BeautifulSoup(res.text,"lxml")

image = soup.select('img')[0]

image