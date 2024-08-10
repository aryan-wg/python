from scraper import scraper,get_page
import json
page = get_page("https://quotes.toscrape.com")
# print(page.get_quotes())
# print(page.get_author())
quotes = page.get_quotes()
authors = page.get_author()
quotes_list = []
for i in range(len(quotes)):
    quotes_list.append({"quote":quotes[i],"author":authors[i]})

json_dump = json.dumps(quotes_list)

output_file = open("output.txt","w")
output_file.write(json_dump)