from my_sqlalchemy.school.models import Students, Group
from my_sqlalchemy.school.sqlalchemy_11 import session1

student_name = input("Enter name for search: ")
students = session1.query(Group, Students).\
    join(Students, Group.id == Students.group_id).filter(Students.firstname==student_name).all()
for gr, st in students:
    print(gr.id, gr.group_name, st.firstname)

