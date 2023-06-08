"""Создать пакет school. Создать файл models.py.
Создать базу school в postgre. Создать таблицу Учебной группы(Group)
с помощью sqlalchemy в декларативном стиле. Группа характеризуется названием(name)."""

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy_utils import database_exists, create_database

DB_USER = "postgres"
DB_PASS = "postgres"
DB_NAME = "school"
DB_ECHO = True
engine = create_engine(f"postgresql://{DB_USER}:{DB_PASS}@localhost/{DB_NAME}", echo=True)
if not database_exists(engine.url):
    create_database(engine.url)

Base = declarative_base()


class Group(Base):
    __tablename__ = "group"
    id = Column(Integer, primary_key=True)
    group_name = Column(String)

    def __init__(self, group_name):
        self.group_name = group_name


class Students(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    group_id = Column(Integer, ForeignKey("group.id"), nullable=False)
    group = relationship("Group", foreign_keys="Students.group_id", backref="students")

    def __init__(self, firstname, lastname, gruop_id):
        self.firstname = firstname
        self.lastname = lastname
        self.group_id = gruop_id


Base.metadata.create_all(engine)