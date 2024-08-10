import re
import requests
from bs4 import BeautifulSoup

class locators:
    PRICE = "article.product_pod div.product_price p.price_color"
    RATING = "article.product_pod p.star-rating"
    LINK = "article.product_pod h3 a"
    NAME = "article.product_pod h3 a"

ratings_to_int = {"One":1,"Two":2,"Three":3,"Four":4,"Five":5}
class scraped:
    def __init__(self,url):
        self.html = requests.get(url).content
        self.data = BeautifulSoup(self.html,"html.parser")

    @property
    def get_names(self):
        names = self.data.select(locators.NAME)
        names = [name.get("title") for name in names]
        return names
    @property
    def get_links(self):
        links = self.data.select(locators.LINK)
        links = [link.get("href") for link in links]
        return links
    @property
    def get_price(self):
        prices = self.data.select(locators.PRICE)
        prices = [price.string for price in prices ]
        return prices
    @property
    def get_rating(self):
        ratings = self.data.select(locators.RATING)
        ratings = [rating.get("class")[1] for rating in ratings]
        return ratings
    @property
    def all_info(self):
        ratings = self.get_rating
        names = self.get_names
        links = self.get_links
        prices = self.get_price
        combined = [{"name":names[i],"price":float(prices[i][1:]),"link":links[i],"rating":ratings_to_int[ratings[i]]} for i in range(len(names))]
        return combined

