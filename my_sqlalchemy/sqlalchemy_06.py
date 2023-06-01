from my_sqlalchemy.book import Book, session1

book1 = Book("book7", 45, "author1", 56, 2000)
book2 = Book("book8", 567, "author2", 89, 2000)
book3 = Book("book9", 458, "author3", 56, 2007)

session1.add_all([book1, book2, book3])
session1.commit()
