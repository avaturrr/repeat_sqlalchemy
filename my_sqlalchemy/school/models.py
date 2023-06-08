"""Создать пакет school. Создать файл models.py.
Создать базу school в postgre. Создать таблицу Учебной группы(Group)
с помощью sqlalchemy в декларативном стиле. Группа характеризуется названием(name)."""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
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


Base.metadata.create_all(engine)
