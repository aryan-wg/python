
def sort_by_rating(books):
    sorted_by_rating = sorted(books,key = lambda book:book["rating"],reverse = True)
    print(sorted_by_rating)

def sort_by_price(books):
    sorted_by_price = sorted(books, key=lambda book: book["price"], reverse=False)
    print(sorted_by_price)