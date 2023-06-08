
from my_sqlalchemy.school.models import Students, Diary
from my_sqlalchemy.school.sqlalchemy_11 import session1

list_students = session1.query(Students).all()
list_diary = []
for st in list_students:
    avg = int(input(f"Enter Greate Point Average for {st.firstname} {st.lastname}: "))
    diary = Diary(avg, st.id)
    list_diary.append(diary)

session1.add_all(list_diary)
session1.commit()