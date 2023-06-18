from my_sqlalchemy.school.models import Students, Book
from my_sqlalchemy.school.sqlalchemy_11 import session1

arr_student = session1.query(Students).all()
arr_book = session1.query(Book).all()
for student in arr_student:
    student.books = arr_book
session1.commit()
