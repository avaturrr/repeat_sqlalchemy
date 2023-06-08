from my_sqlalchemy.school.models import Students
from my_sqlalchemy.school.sqlalchemy_11 import session1

student_1 = Students("f1", "l1", 1)
student_2 = Students("f2", "l2", 1)
student_3 = Students("f3", "l3", 1)
student_4 = Students("f4", "l4", 2)
student_5 = Students("f5", "l5", 2)
student_6 = Students("f6", "l6", 2)

session1.add_all([student_6, student_5, student_4, student_3, student_2, student_1])
session1.commit()
