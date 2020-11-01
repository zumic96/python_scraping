import requests
import bs4
import lxml

res = requests.get("http://www.example.com")

soup = bs4.BeautifulSoup(res.text,"lxml")
soup.select('title')[0].getText()

site_paragraphs = soup.select('p')
site_paragraphs[0].getText()