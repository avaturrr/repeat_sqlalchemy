from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///sa_test.db")
connection = engine.connect()
trans = connection.begin()
title_u = input("Enter title: ")
pages_u = int(input("Enter pages: "))
author_u = input("Enter author: ")
price_u = int(input("Enter price: "))
release_year_u = int(input("Enter release year: "))
user_choice = input("Do you want save book? (y or n)")

insert_book = ("""insert into Book (title, pages, author, price, release_year) values 
(:title_u, :pages_u, :author_u, :price_u, :release_year_u)""")
query = text(insert_book).bindparams(title_u=title_u, pages_u=pages_u, author_u=author_u,
                                     price_u=price_u, release_year_u=release_year_u)
connection.execute(query)
if user_choice == "y":
    trans.commit()
else:
    trans.rollback()
connection.close()
