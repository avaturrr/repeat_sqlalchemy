from my_sqlalchemy.library.bl import create, read, update, delete, filter_by_author


def main():
    user_choice = int(input("Enter number of function:\n 1. create\n"
                            "2. read\n 3. update\n 4. delete\n"
                            "5. filter by author\n"))
    dict_func = {1: create, 2: read, 3: update, 4: delete, 5: filter_by_author}
    dict_func[user_choice]()


if __name__ == "__main__":
    main()
