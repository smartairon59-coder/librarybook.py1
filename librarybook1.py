import sqlite3
import pandas as pd

# ---- Paert 1: What is a JOIN - Build and cExplore the Tables ----

conn = sqlite3.connect(':memory:')

conn.execute("""CREATE TABLE author (
    author_id INTERGER PRIMARY KEY,
    author_name TEXT NOT NULL UNIQUE
)""")

conn.executemany("INSERT INTO author VALUES(?, ?)",[
    (1, 'Roald Dahl'),
    (2, 'J.K. Rowling'),
    (3, 'Rick Riordan'),
    (4, 'Jeff Kinney,'),
    (5, 'Day Pilkey'),
    (6, 'Lemony Snicket,'),
])

conn.executemany("INSERT INTO book VALUES(?,?,?)",[
    (1, 'Charlie and the Choclate Factory',       1),
    (2, 'James and the Giang Peach',             2),
    (3, 'Harry Potter and the Philosophers stone',3),
    (4, 'Harry Potter and the Chamber of Secrets',4),
    (5, 'The Lightning Thief',                   5),
    (6, 'The Sea of Monsters',                    6),
    (7, 'Diary of a Wimpy Kid',                  7),

])

conn.commit()

authors = pd.read_sql("SELECT * FROM author", conn)
books   = pd.read_sql("SELECT * FROM book", conn)
print("Author Tale:")
print(authors)
print()
print("Book table:")
print(books)
print()

inner = pd.read_sql(
    "SELECT author.authoer_name, book.book_title "
    "FROM author INNER join book ON authot .author_id = book.author_id",
    conn
)
print("INNER JOIN - authors mathced with their books:")
print(inner)
print()

left = pd.read_sql(
   "SELECT autho.author_name, boo.book_title "
   "FROM author LEFT JOIN book ON authoer.author_id = book.author_id",
   conn
)
print(inner)
print()

left = pd.read_sql(
    "SELECTauthor.author_name, book.book_title "
)