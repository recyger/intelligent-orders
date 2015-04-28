# -*- coding: utf-8 -*-
"""
 Created by Fuoco on 05.04.2015 for intelligeman
"""
__author__ = 'Fuoco'
__credits__ = ["Fuoco"]
__license__ = "GPL"
__version__ = "0.0.1"
__email__ = "recyger@gmail.com"

from .init import app

@app.post('/menu')
def menu():
    return {
        'data': [
            {
                'value': 'driver',
                'name': '<i class="fa fa-users"></i> Водители',
            },
            {
                'value': 'truck',
                'name': '<i class="fa fa-truck"></i> Машины',
            },
            {
                'value': 'order',
                'name': '<i class="fa fa-table"></i> Закакзы',
            },
            {
                'value': 'transportation',
                'name': '<i class="fa fa-road"></i> Маршруты',
            },
            {
                'value': 'address',
                'name': '<i class="fa fa-map-marker"></i> Адреса',
            },
            {
                'value': 'customer',
                'name': '<i class="fa fa-user-secret"></i> Заказчики',
            },
            {
                'name': '<i class="fa fa-list-ul"></i> Типы и Статусы <span class="caret"></span>',
                'items': [
                    {
                        'value': 'driver_status',
                        'name': '<i class="fa fa-users"></i> Статусы водителей'
                    },
                    {
                        'value': 'truck_model',
                        'name': '<i class="fa fa-truck"></i> Модели машин'
                    },
                    {
                        'value': 'truck_status',
                        'name': '<i class="fa fa-truck"></i> Статусы машин'
                    },
                    {
                        'value': 'order_status',
                        'name': '<i class="fa fa-table"></i> Статусы заказов'
                    },
                    {
                        'value': 'transportation_status',
                        'name': '<i class="fa fa-road"></i> Статусы маршрутов'
                    }
                ]
            }
        ]
    }