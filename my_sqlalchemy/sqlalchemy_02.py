from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///sa_test.db")
with engine.connect() as connection:
    insert_values = """insert into Book (title, pages, author, price, release_year) values 
    ("book1", 12, "a1", 10, 1990),
    ("book2", 34, "a2", 34, 2000),
    ("book3", 17, "a3", 89, 2008),
    ("book4", 98, "a4", 7, 1998),
    ("book5", 90, "a5", 34, 1989);"""
    query = text(insert_values)
    connection.execute(query)
    connection.commit()
