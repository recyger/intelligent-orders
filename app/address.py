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
from db import db_session, select, Address

@app.post('/address/list')
@db_session
def address_list():
    result = {
        'data': {},
    }
    for item in select(i for i in Address):
        result['data'][item.id] = item.to_dict()
    return result

@app.post('/address/save')
@db_session
def address_save():
    _id, data = Tool.get_post('status')
    if _id is not None:
        user = Address[_id]
        user.set(**data)
    else:
        Address(**data)

@app.post('/address/delete/:user_id')
@db_session
def address_delete(user_id):
    model = Address[int(user_id)]
    if model:
        model.delete()
        return {
            'result': 'success',
        }
    abort(400, 'Не найден пользователь')

@app.post('/address/get/:ids')
@db_session
def address_get(ids):
    model = Address[int(ids)]
    if model:
        return {
            'data': model.to_dict(),
        }
    abort(400, 'Не найден пользователь')