from sqlalchemy import text, create_engine

from my_sqlalchemy.my_exception import MyException

user_year = input("Enter year: ")
if not user_year.isdigit():
    raise MyException
engine = create_engine("sqlite:///sa_test.db")
with engine.connect() as connection:
    filter_by_year = (f"""select * from Book where release_year < {int(user_year)}""")
    query = text(filter_by_year)
    filtred_data = connection.execute(query)

list_filtred_book = []
for book in filtred_data:
    list_filtred_book.append(book)
if list_filtred_book:
    print(list_filtred_book)
else:
    print("NOT FOUND")
