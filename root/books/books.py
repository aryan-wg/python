from utils import database

"""
book structure will be 
{
    title:"string"
    author:"string"
    read:"bool"
}
"""

while True:
    operation = input("Press \na-to add a book\nd-to delete a book\nr-to mark a book read\nl-to list all the books\nq-to quit this program \n")
    # print(operation)
    # print(operation=="a")
    if operation == "a":
        book_name = input("Enter book name \n").title().strip()
        author = input("Enter the name of the author \n").title().strip()
        book = dict({"name":book_name,"author":author,"read":False})
        print(database.add_book(book)["name"] + " is added to the library.")  
    elif operation == "d":
        book_to_delete = input("Enter book you want to remove").title().strip()
        database.remove_book(book_to_delete)
    elif operation == "r":
        book_read = input("Enter book that you read").title().strip()
        database.mark_as_read(book_read)
    elif operation == "l":
        print("List all the books")
        print(database.get_all())
    elif operation == "q":
        break