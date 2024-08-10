from selenium import webdriver
from quotes import quotesPage
print("hello")
chrome = webdriver.Edge()
print("hello")
chrome.get("https://quotes.toscrape.com/search.aspx")
quotes = quotesPage(chrome)
print(quotes.get_quote())
# input("give me something")
