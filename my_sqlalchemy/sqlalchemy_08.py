from sqlalchemy import and_

from my_sqlalchemy.book import session1, Book, my_table

start_year = int(input("Enter start year: "))
finish_year = int(input("Enter finish year: "))
book_filtered = session1.query(Book).filter(and_(Book.release_year > start_year,
                                                 Book.release_year < finish_year))
list_book = list(book_filtered)
if list_book:
    for i in book_filtered:
        print(i.id, i.title, i.author)
else:
    print("NOT FOUND")
