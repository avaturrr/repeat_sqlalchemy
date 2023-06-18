from bl import create_brand, create_car, \
    update_car, update_brand, read_car, read_brand, \
    delete_car, delete_brand


def main():
    user_choice = {"1": create_brand, "2": create_car,
                   "3": update_brand, "4": update_car,
                   "5": read_brand, "6": read_car,
                   "7": delete_brand, "8": delete_car}
    user_input = input("select options and enter number\n"
                       "1:create brand\n"
                       "2:create car\n"
                       "3:update brand\n"
                       "4:update car\n"
                       "5:read brand\n"
                       "6:read car\n"
                       "7:delete brand\n"
                       "8:delete car\n")
    user_choice[user_input]()


if __name__ == "__main__":
    main()
