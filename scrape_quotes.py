import requests
import bs4
import lxml

# Get title of every book with 2 star rating
base_url = 'http://quotes.toscrape.com/page/{}/'
# Select authors form first page
authors_first_page = []
res = requests.get(base_url.format(1))
soup = bs4.BeautifulSoup(res.text,'lxml')
for author in soup.select('.author'):
    authors_first_page.append(author.text)
print(authors_first_page)

# Select all quotes form first page
quotes_first_page = []
res = requests.get(base_url.format(1))
soup = bs4.BeautifulSoup(res.text,'lxml')
for quote in soup.select('.text'):
    quotes_first_page.append(quote.text)
print(quotes_first_page)

# Select top 10 tags from first page
tags_first_page = []
res = requests.get(base_url.format(1))
soup = bs4.BeautifulSoup(res.text,'lxml')
top_ten = soup.find('div', {'class': 'col-md-4 tags-box'})
for tag in top_ten.findAll('span'):
    tags_first_page.append(tag.select('a')[0].text)
print(tags_first_page)

# Get unique authors from all pages
page_num = 0
continue_scrape = True
unique_authors = set()
while continue_scrape:
    page_num += 1
    res = requests.get(base_url.format(page_num))
    soup = bs4.BeautifulSoup(res.text,'lxml')
    if 'No quotes found!' in soup.select('.col-md-8')[1].text:
        continue_scrape = False
        break
    else:
        for author in soup.select('.author'):
            unique_authors.add(author.text)
print(unique_authors)
