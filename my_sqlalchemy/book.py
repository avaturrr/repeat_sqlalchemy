from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker, registry

engine = create_engine("sqlite:///book.db")
metadata = MetaData()
my_table = Table("Book", metadata,
                 Column("id", Integer, primary_key=True),
                 Column("title", String),
                 Column("pages", Integer),
                 Column("author", String),
                 Column("price", Integer),
                 Column("release_year", Integer))
metadata.create_all(engine)


class Book:
    def __init__(self, title, pages, author, price, release_year):
        self.title = title
        self.pages = pages
        self.author = author
        self.price = price
        self.release_year = release_year


mapper_registry = registry()
mapper_registry.map_imperatively(Book, my_table)
Session = sessionmaker(bind=engine)
session1 = Session()
