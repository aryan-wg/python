import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

# cursor.execute("sql query")
cursor.execute('CREATE TABLE Books(name text primary key, author text, read integer)')
connection.commit()

connection.close()