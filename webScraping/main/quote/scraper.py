import requests
from bs4 import BeautifulSoup

class quotes_locators :
    AUTHOR_LOCATOR = 'body div.container div.row div.quote small'
    QUOTE_LOCATOR = 'body div.container div.row div.quote span.text'
class scraper:
    def __init__(self,page):
        self.soup = BeautifulSoup(page.content,"html.parser")
    def get_quotes(self):
        quotes = self.soup.select(quotes_locators.QUOTE_LOCATOR)
        quotes = [ quote.string for quote in quotes ]
        return quotes
    def get_author(self):
        authors = self.soup.select(quotes_locators.AUTHOR_LOCATOR)
        authors = [ author.string for author in authors]
        return authors

def get_page(url):
   page = requests.get(url)
   return scraper(page)
