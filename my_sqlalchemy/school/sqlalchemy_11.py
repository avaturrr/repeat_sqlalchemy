"""Создать файл sqlalchemy_11.py. Создать две группы. Добавить в каждую по три студента.
"""
from sqlalchemy.orm import sessionmaker

from my_sqlalchemy.school.models import Group, engine

Session = sessionmaker(bind=engine)
session1 = Session()

group_1 = Group("qwe1")
group_2 = Group("qwe2")

session1.add_all([group_1, group_2])
session1.commit()