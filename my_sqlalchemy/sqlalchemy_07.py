from my_sqlalchemy.book import session1, Book

all_book = session1.query(Book)
for book in all_book:
    print(book.release_year, book.title, book.author)