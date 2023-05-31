from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///sa_test.db")
with engine.connect() as connection:
    creat_table = """create table Book 
    (id integer primary key autoincrement,
    title varchar,
    pages integer,
    author varchar,
    price float,
    release_year integer)"""
    query = text(creat_table)
    connection.execute(query)
