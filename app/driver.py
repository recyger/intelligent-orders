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
from db import db_session, select, Driver_Status, Driver

@app.post('/driver_status/list')
@db_session
def driver_status_list():
    result = {
        'data': {},
    }
    for item in select(i for i in Driver_Status):
        result['data'][item.id] = item.to_dict()
    return result

@app.post('/driver_status/save')
@db_session
def driver_status_save():
    _id, data = Tool.get_post('status')
    if _id is not None:
        user = Driver_Status[_id]
        user.set(**data)
    else:
        Driver_Status(**data)

@app.post('/driver_status/delete/:user_id')
@db_session
def driver_status_delete(user_id):
    model = Driver_Status[int(user_id)]
    if model:
        model.delete()
        return {
            'result': 'success',
        }
    abort(400, 'Не найден пользователь')

@app.post('/driver/list')
@app.post('/driver/list/:status')
@db_session
def driver_list(status=None):
    result = {
        'data': {},
    }
    if status:
        items = select(i for i in Driver if i.status == status)
    else:
        items = select(i for i in Driver)
    for item in items:
        result['data'][item.id] = item.to_dict()
        result['data'][item.id]['full_name'] = item.name + ' ' + item.patronymic + ' ' + item.surname
    return result

@app.post('/driver/save')
@db_session
def driver_save():
    _id, data = Tool.get_post('status')
    if _id is not None:
        user = Driver[_id]
        user.set(**data)
    else:
        Driver(**data)

@app.post('/driver/delete/:user_id')
@db_session
def driver_delete(user_id):
    model = Driver[int(user_id)]
    if model:
        model.delete()
        return {
            'result': 'success',
        }
    abort(400, 'Не найден пользователь')