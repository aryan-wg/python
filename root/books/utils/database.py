""" this file will be conserned with storing and retriving data from a list """
# from .... import another_file_in_root 

# another_file_in_root.print_another()
books = []

def add_book(book):
    books.append(book)
    return books[len(books)-1]

def remove_book(book_name):
    global books
    books = filter(lambda book: book["name"]!=book_name,books)
    books = list(books)

def get_all():
    return books

def mark_as_read(book_name):
    for book in books :
        if book.name == book_name :
            book.read = True
            return "Marked as read" 
    else:
        return "Book was not found"

print("hello")