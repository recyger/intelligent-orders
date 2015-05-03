# -*- coding: utf-8 -*-
"""
 Created by Fuoco on 05.04.2015 for intelligeman
"""
__author__ = 'Fuoco'
__credits__ = ["Fuoco"]
__license__ = "GPL"
__version__ = "0.0.1"
__email__ = "recyger@gmail.com"

from .init import app, Tool, abort
from db import db_session, select, Truck_Model, Truck_Status, Truck

@app.post('/truck_model/list')
@db_session
def truck_model_list():
    result = {
        'data': {},
    }
    for item in select(i for i in Truck_Model):
        result['data'][item.id] = item.to_dict()
    return result

@app.post('/truck_model/save')
@db_session
def truck_model_save():
    _id, data = Tool.get_post('status')
    if _id is not None:
        user = Truck_Model[_id]
        user.set(**data)
    else:
        Truck_Model(**data)

@app.post('/truck_model/delete/:user_id')
@db_session
def truck_model_delete(user_id):
    model = Truck_Model[int(user_id)]
    if model:
        model.delete()
        return {
            'result': 'success',
        }
    abort(400, 'Не найден пользователь')

@app.post('/truck_status/list')
@db_session
def truck_status_list():
    result = {
        'data': {},
    }
    for item in select(i for i in Truck_Status):
        result['data'][item.id] = item.to_dict()
    return result

@app.post('/truck_status/save')
@db_session
def truck_status_save():
    _id, data = Tool.get_post('status')
    if _id is not None:
        user = Truck_Status[_id]
        user.set(**data)
    else:
        Truck_Status(**data)

@app.post('/truck_status/delete/:user_id')
@db_session
def truck_status_delete(user_id):
    model = Truck_Status[int(user_id)]
    if model:
        model.delete()
        return {
            'result': 'success',
        }
    abort(400, 'Не найден пользователь')

@app.post('/truck/list')
@app.post('/truck/list/:status')
@db_session
def truck_list(status=None):
    result = {
        'data': {},
    }
    if status:
        items = select(i for i in Truck if i.status == status)
    else:
        items = select(i for i in Truck)
    for item in items:
        result['data'][item.id] = item.to_dict(only=['id', 'number', 'model', 'status'])
    return result

@app.post('/truck/save')
@db_session
def truck_save():
    _id, data = Tool.get_post('status')
    if _id is not None:
        user = Truck[_id]
        user.set(**data)
    else:
        Truck(**data)

@app.post('/truck/delete/:user_id')
@db_session
def truck_delete(user_id):
    model = Truck[int(user_id)]
    if model:
        model.delete()
        return {
            'result': 'success',
        }
    abort(400, 'Не найден пользователь')