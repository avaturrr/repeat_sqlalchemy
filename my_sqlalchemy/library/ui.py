def ui_create():
    title = input("Enter title: ")
    pages = int(input("Enter pages: "))
    author = input("Enter author: ")
    price = int(input("Enter price: "))
    release_year = int(input("Enter release_year: "))
    new_book = (title, pages, author, price, release_year)
    return new_book


def ui_read():
    selected_id = input("Enter book id or word 'all': ")
    return selected_id


def ui_update():
    selected_id = input("Enter book id: ")
    selected_column = input("Enter column name to update: ")
    dict_types = {"title": "", "pages": "int", "author": "", "price": "int", "release_year": "int"}
    new_value = (input("Enter new value: "))
    return selected_id, selected_column, new_value


def ui_delete():
    selected_id = int(input("Enter book id to delete: "))
    return selected_id


def ui_filter_by_author():
    selected_author = input("Enter author: ")
    return selected_author
