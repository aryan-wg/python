from scraper import scraped
from utilities import sort_by_rating,sort_by_price

books_scraped = scraped("https://books.toscrape.com/catalogue/page-1.html")

# books_scraped.get_price
# print(books_scraped.all_info)

sort_by_rating(books_scraped.all_info)
sort_by_price(books_scraped.all_info)
