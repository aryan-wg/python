from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
class quotes_locators:
    # AUTHOR_LOCATOR = 'author'
    AUTHOR_LOCATOR = 'select[id="author"]'
    QUOTE_LOCATOR = 'tag'
class quotesPage:
    def __init__(self,browser):
        self.browser = browser
    def get_quote(self):
        all_authors = self.browser.find_element(By.CSS_SELECTOR,quotes_locators.AUTHOR_LOCATOR)
        # array_authors= [element.text.strip() for element in Select(all_authors[0]).options][1::]
        # print(all_authors[0])
        array_authors = all_authors.text.split("\n")
        array_authors = [option.strip() for option in array_authors[4::2]]
        print(array_authors)
        for author in array_authors:
            # option = "Albert Einstein"
            # author  = "J.K. Rowling"
            print(author)
            print(all_authors)
            Select(all_authors).select_by_visible_text(author)
            all_tags = self.browser.find_element(By.ID, quotes_locators.QUOTE_LOCATOR)
            print(all_tags.text)
            # print(Select(all_tags).options)
            print("new one starts from here -------------------------------------------------")
        # print(elements.visible_text)
        # print(all_authors)
        # all_quotes  = [quote_element.text for quote_element in all_quote_elements]
        return all_authors

