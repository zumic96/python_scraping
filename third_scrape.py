import requests
import bs4
import lxml

res = requests.get("https://hr.wikipedia.org/wiki/Deep_Blue")

soup = bs4.BeautifulSoup(res.text,"lxml")

image = soup.select('.thumbimage')[0]

image['src']

image_link = requests.get(f"https:{image'src']}")

f = open('test.jpg','wb')
f.write(image_link.content)
f.close()