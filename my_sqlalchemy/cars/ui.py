def new_brand():
    name = input("Enter brand name: ")
    return name


def new_car():
    model = input("Enter car model: ")
    release_year = int(input("Enter release year: "))
    brand = input("Enter brand id: ")
    new_car_list = (model, release_year, brand)
    return new_car_list


def ui_update_brand():
    brand_for_update = input("Enter brand id for update: ")
    new_brand_name = input("Enter new name for brand: ")
    return brand_for_update, new_brand_name


def ui_update_car():
    car_for_update = input("Enter car id for update: ")
    new_car_model = input("Enter car model: ")
    new_car_release_year = int(input("Enter car release year: "))
    new_car_brand = input("Enter car brand_id: ")
    return car_for_update, new_car_model, new_car_release_year, new_car_brand


def ui_read_brand():
    brand_read = int(input("Enter id brand for reading: "))
    return brand_read


def ui_read_car():
    car_read = int(input("Enter id car for reading: "))
    return car_read


def ui_delete_brand():
    brand_delete = int(input("Enter id brand for deleting: "))
    return brand_delete


def ui_delete_car():
    car_delete = int(input("Enter id car for deleting: "))
    return car_delete
