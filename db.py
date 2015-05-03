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
    refills = Set("Refills")


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
    refills = Set("Refills")


class Truck_Model(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    expense = Optional(str, default=' ')
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
    cost = Required(str)


class Address(db.Entity):
    id = PrimaryKey(int, auto=True)
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
    data = Required(datetime, default=datetime.now())
    value = Required(str)
    mileage = Optional(str)


class Refills(db.Entity):
    id = PrimaryKey(int, auto=True)
    driver = Required(Driver)
    truck = Required(Truck)
    date = Required(datetime, default=datetime.now())
    value = Required(str)
    cost = Required(str)


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
        Truck_Model(name=u'Ивеко')
        Truck_Model(name=u'Скания')

    if count(r for r in Truck_Status) == 0:
        Truck_Status(name=u'В простое')
        Truck_Status(name=u'На маршруте')
        Truck_Status(name=u'На ремонте')
        Truck_Status(name=u'Списан')

    if count(r for r in Order_Status) == 0:
        Order_Status(name=u'Выполняется')
        Order_Status(name=u'Завершен')


init()