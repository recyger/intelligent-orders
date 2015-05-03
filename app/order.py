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
from db import db_session, select, Order, Order_Status

@app.post('/order_status/list')
@db_session
def order_status_list():
    result = {
        'data': {},
    }
    for item in select(i for i in Order_Status):
        result['data'][item.id] = item.to_dict()
    return result

@app.post('/order_status/save')
@db_session
def order_status_save():
    _id, data = Tool.get_post('status')
    if _id is not None:
        user = Order_Status[_id]
        user.set(**data)
    else:
        Order_Status(**data)

@app.post('/order_status/delete/:user_id')
@db_session
def order_status_delete(user_id):
    model = Order_Status[int(user_id)]
    if model:
        model.delete()
        return {
            'result': 'success',
        }
    abort(400, 'Не найден пользователь')

@app.post('/order/list')
@app.post('/order/list/:status')
@db_session
def order_list(status=None):
    result = {
        'data': {},
    }
    if status:
        items = select(i for i in Order if i.status == status)
    else:
        items = select(i for i in Order)

    for item in items:
        result['data'][item.id] = item.to_dict()
        result['data'][item.id]['processed_value'] = 0
        for t in item.transportations:
            result['data'][item.id]['processed_value'] += float(t.value)
    return result

@app.post('/order/save')
@db_session
def order_save():
    _id, data = Tool.get_post('status')
    if _id is not None:
        user = Order[_id]
        user.set(**data)
    else:
        if 'status' not in data.keys():
            data['status'] = 1
        Order(**data)

@app.post('/order/delete/:user_id')
@db_session
def order_delete(user_id):
    model = Order[int(user_id)]
    if model:
        model.delete()
        return {
            'result': 'success',
        }
    abort(400, 'Не найден пользователь')