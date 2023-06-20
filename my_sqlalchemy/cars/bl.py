from sqlalchemy.orm import sessionmaker

from my_sqlalchemy.cars.models import engine, Brand, Car
from my_sqlalchemy.cars.ui import new_brand, new_car, ui_update_brand, ui_update_car, ui_read_brand, ui_read_car, \
    ui_delete_brand, ui_delete_car

Session = sessionmaker(bind=engine)
session1 = Session()


def create_brand():
    brand_name = new_brand()
    brand_new = Brand(brand_name)
    session1.add(brand_new)
    session1.commit()
    session1.close()


def create_car():
    car_name = new_car()
    car_new = Car(car_name[0], car_name[1], car_name[2])
    session1.add(car_new)
    session1.commit()
    session1.close()


def update_brand():
    id_brand_for_update = ui_update_brand()
    brand_for_update = session1.query(Brand).get(id_brand_for_update[0])
    brand_for_update.name = id_brand_for_update[1]
    session1.commit()
    session1.close()


def update_car():
    id_car_for_update = ui_update_car()
    car_for_update = session1.query(Car).filter_by(id=id_car_for_update[0])
    car_for_update.model = id_car_for_update[1]
    car_for_update.release_year = id_car_for_update[2]
    car_for_update.brand_id = id_car_for_update[3]
    session1.commit()
    session1.close()


def read_brand():
    brand = session1.query(Brand).get(ui_read_brand())
    print(brand.id, brand.name)
    session1.close()


def read_car():
    car = session1.query(Car).get(ui_read_car())
    print(car.id, car.model, car.release_year, car.brand_id)
    session1.close()


def delete_brand():
    brand = ui_delete_brand()
    car_delete = session1.query(Car).filter_by(brand_id=brand).first()
    print(car_delete)
    session1.delete(car_delete)
    session1.commit()
    session1.close()
    brand_delete = session1.query(Brand).get(brand)
    session1.delete(brand_delete)
    session1.commit()
    session1.close()


def delete_car():
    car = session1.query(Car).get(ui_delete_car())
    session1.delete(car)
    session1.commit()
    session1.close()
