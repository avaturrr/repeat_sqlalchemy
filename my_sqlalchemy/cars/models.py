from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy_utils import database_exists, create_database

DB_USER = "postgres"
DB_PASS = "postgres"
DB_NAME = "test2"
DB_ECHO = True
engine = create_engine(f"postgresql://{DB_USER}:{DB_PASS}@localhost/{DB_NAME}", echo=DB_ECHO)
if not database_exists(engine.url):
    create_database(engine.url)

Base = declarative_base()


class Brand(Base):
    __tablename__ = "brand"
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name


class Car(Base):
    __tablename__ = "car"
    id = Column(Integer, primary_key=True)
    model = Column(String)
    release_year = Column(Integer)
    brand_id = Column(Integer, ForeignKey("brand.id"), nullable=False)
    brand = relationship("Brand", foreign_keys="Car.brand_id", backref="cars")

    def __init__(self, model, release_year, brand_id):
        self.model = model
        self.release_year = release_year
        self.brand_id = brand_id


Base.metadata.create_all(engine)
