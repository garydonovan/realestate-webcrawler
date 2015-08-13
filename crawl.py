import requests
from bs4 import BeautifulSoup

def house_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'http://www.realestate.com.au/buy/property-house-with-3-bedrooms-between-400000-any-in-wantirna%2c+vic+3152/list-' + str(page) + '?maxBeds=any&activeSort=price-desc&source=location-search'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        for link in soup.findAll('a', {'name'}):
            href = "http://realestate.com.au" + link.get('href')
            title = link.string
            print(href)
            print(title)
        page += 1

house_spider(2)
