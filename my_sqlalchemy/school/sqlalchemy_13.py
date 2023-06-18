from my_sqlalchemy.school.models import Book, Students
from my_sqlalchemy.school.sqlalchemy_11 import session1

arr_book = [Book("math", 20),
          Book("physic", 280),
          Book("cs", 720),
          Book("biology", 205),
          Book("f", 45)]

session1.add_all(arr_book)
session1.commit()
