import sqlite3
import pandas as pd

#part 1

conn = sqlite3.connect(':memory:')

conn.execute("""create table author (
    author_id   integer primary key,
    author__name text not null unique
)""")

conn.execute("""create table book(
    book_id      integerr primary key,
    book_title   text not null,
    author_id    integer
)""")

conn.executemany("Insert into author values (?, ?)", [
    (1, 'Roald Dhal'),
    (2, 'J.K Rowling'),
    (3, 'Rick Riodan'),
    (4, 'Jeff Kenney'),
    (5, 'Dav Pilkey'),
    (6, 'Lemony Snicket'),
])

conn.executemany("Insert into book values(?, ?, ?)", [
    (1, 'Charlie and the Chocolate Factory',       1),
    (2, 'James and the Giant Peach',       1),
    (3, 'Harry Potter and the Philisophers stone',       2),
    (4, 'Harry Potter and the CHamber of Secrets',       2),
    (5, 'The Lighting Theif',       3),
    (6, 'The Sea of Monsters',       4),
    (7, 'Diary of a Wimpy Kid',       4),
])

conn.commit()
authors = pd.read_sql("Select * from author", conn)
book    = pd.read_sql("select * from book", conn)
print("AUthor table:")
print(authors)
print()
print("Book tabale:")
print(book)
print()

# part 2

inner = pd.read_sql(
    "select author.authgor_name, book.book_title "
    "From author inner join book on author.author_id = book.author_id", 
    conn
)
print("Left Join -authors matched with their books:")
print(inner)
print()

#Part 3
left = pd.read_sql(
    "select author.author_name, book.book_title "
    "from author left join book on author.author_id = book." \
    "author_id",
    conn
)
print("Left join - all authors, null where book found:")
print(left)
print()

#part 4
cross = pd.read_sql(
    "select author.author_name,  book.book_title "
    "from author CROSS JOIN book where author.author_id <= 2",
    conn 
)
print("CROSS JOIN - first 2 authors paired with every book:")
print(cross)
print()

#part 5

union = pd.read_sql(
    "select suthor_name as name, 'Author' as type from author"
    "union"
    "select book_title as name, 'book' as type from book",
    conn
)
print("Union - all author names and book titles combined:")
print(union)

conn.close()
