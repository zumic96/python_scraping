import requests
import bs4
import lxml

# Get title of every book with 2 star rating
base_url = 'http://books.toscrape.com/catalogue/page-{}.html'
two_star_titles = []
for n in range (1,51):
    res = requests.get(base_url.format(n))
    soup = bs4.BeautifulSoup(res.text,'lxml')
    books = soup.select('.product_pod')
    for book in books:
        if len(book.select(".star-rating.Two")) != 0:
            two_star_titles.append(book.select("a")[1]['title'])
