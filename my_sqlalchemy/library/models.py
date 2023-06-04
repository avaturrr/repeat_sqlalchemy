from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///library.db")
connection = engine.connect()
Base = declarative_base()


class Book(Base):
    __tablename__ = "book"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    pages = Column(Integer)
    author = Column(String)
    price = Column(Integer)
    release_year = Column(Integer)

    def __init__(self, title, pages, author, price, release_year):
        self.title = title
        self.pages = pages
        self.author = author
        self.price = price
        self.release_year = release_year


Base.metadata.create_all(engine)
