# -*- coding: utf-8 -*-
"""
 Created by Fuoco on 03.04.2015 for intelligeman
"""
__author__ = 'Fuoco'
__credits__ = ["Fuoco"]
__license__ = "GPL"
__version__ = "0.0.1"
__email__ = "recyger@gmail.com"

from datetime import datetime
from pony.orm import *

db = Database("sqlite", "database.sqlite", create_db=True)

class Driver(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str, 128)
    patronymic = Required(str, 128)
    surname = Required(str, 128)
    status = Required("Driver_Status")
    transportations = Set("Transportation")


class Driver_Status(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str, 128)
    drivers = Set(Driver)


class Truck(db.Entity):
    id = PrimaryKey(int, auto=True)
    number = Required(str)
    model = Required("Truck_Model")
    registration = Required(datetime, default=datetime.now())
    status = Required("Truck_Status")
    transportations = Set("Transportation")


class Truck_Model(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    trucks = Set(Truck)


class Truck_Status(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    trucks = Set(Truck)


class Customer(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    orders = Set("Order")


class Order(db.Entity):
    id = PrimaryKey(int, auto=True)
    customer = Required(Customer)
    name = Required(str)
    value = Required(str)
    address = Required("Address")
    status = Required("Order_Status")
    transportations = Set("Transportation")


class Address(db.Entity):
    id = PrimaryKey(int, auto=True)
    coordinates = Required(str, default=' ')
    name = Required(str)
    os = Set(Order)
    departures = Set("Transportation", reverse="departure")
    destinations = Set("Transportation", reverse="destination")


class Order_Status(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    orders = Set(Order)


class Transportation(db.Entity):
    id = PrimaryKey(int, auto=True)
    departure = Required(Address, reverse="departures")
    destination = Required(Address, reverse="destinations")
    order = Required(Order)
    driver = Required(Driver)
    truck = Required(Truck)
    status = Required("Transportation_Status")
    start = Required(datetime, default=datetime.now())
    end = Optional(datetime)
    value = Required(str)
    fuel = Optional(str)
    mileage = Optional(str)


class Transportation_Status(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    transportations = Set(Transportation)


sql_debug(True)
db.generate_mapping(create_tables=True)

@db_session
def init():
    if count(s for s in Driver_Status) == 0:
        Driver_Status(name=u'На месте')
        Driver_Status(name=u'На маршруте')
        Driver_Status(name=u'В отпуске')
        Driver_Status(name=u'Уволен')

    if count(r for r in Truck_Model) == 0:
        Truck_Model(name=u'Урал')
        Truck_Model(name=u'КАМАЗ')

    if count(r for r in Truck_Status) == 0:
        Truck_Status(name=u'На месте')
        Truck_Status(name=u'На маршруте')
        Truck_Status(name=u'На ремонте')
        Truck_Status(name=u'Списан')

    if count(r for r in Order_Status) == 0:
        Order_Status(name=u'В обработке')
        Order_Status(name=u'Выполняется')
        Order_Status(name=u'Завершен')

    if count(r for r in Transportation_Status) == 0:
        Transportation_Status(name=u'В обработке')
        Transportation_Status(name=u'Выполняется')
        Transportation_Status(name=u'Завершен')


init()