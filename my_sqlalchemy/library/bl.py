from sqlalchemy.orm import sessionmaker

from my_sqlalchemy.library.models import Book, engine
from my_sqlalchemy.library.ui import ui_create, ui_read, ui_update, ui_delete, ui_filter_by_author


def create():
    new_book = ui_create()
    Session = sessionmaker(bind=engine)
    session = Session()
    created_book = Book(new_book[0], new_book[1], new_book[2], new_book[3], new_book[4])
    session.add(created_book)
    session.commit()
    session.close()


def read():
    selected_book = ui_read()
    Session = sessionmaker(bind=engine)
    session = Session()
    if selected_book == "all":
        selected_book_list = session.query(Book)
        for book in selected_book_list:
            print(book.id, book.title, book.author, book.price)
    else:
        selected_book = session.query(Book).get(int(selected_book))
        print(selected_book.id, selected_book.title, selected_book.author,
              selected_book.price, selected_book.release_year)
    session.close()


def update():
    book_id_column_value = ui_update()
    Session = sessionmaker(bind=engine)
    session = Session()
    update_book = session.query(Book).get(int(book_id_column_value[0]))
    update_book.book_id_column_value[1] = book_id_column_value[2]
    session.commit()
    session.close()


def delete():
    selected_book_id = ui_delete()
    Session = sessionmaker(bind=engine)
    session = Session()
    book_delete = session.query(Book).get(selected_book_id)
    session.delete(book_delete)
    session.commit()
    session.close()


def filter_by_author():
    selected_author = ui_filter_by_author()
    Session = sessionmaker(bind=engine)
    session = Session()
    list_filtered_book = session.query(Book).filter_by(author=selected_author)
    for book in list_filtered_book:
        print(book.id, book.title, book.pages, book.price)
    session.close()
