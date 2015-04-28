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
from db import db_session, select, Customer

@app.post('/customer/list')
@db_session
def customer_list():
    result = {
        'data': {},
    }
    for item in select(i for i in Customer):
        result['data'][item.id] = item.to_dict()
    return result

@app.post('/customer/save')
@db_session
def customer_save():
    data = Tool.get_post('status')
    _id = None
    if 'id' in data.keys():
        _id = int(data['id'])
        del data['id']
    if _id is not None:
        user = Customer[_id]
        user.set(**data)
    else:
        Customer(**data)

@app.post('/customer/delete/:user_id')
@db_session
def customer_delete(user_id):
    model = Customer[int(user_id)]
    if model:
        model.delete()
        return {
            'result': 'success',
        }
    abort(400, 'Не найден пользователь')