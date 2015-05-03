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
from db import db_session, select, Transportation


@app.post('/transportation/list')
@db_session
def transportation_list():
    result = {
        'data': {},
    }
    for item in select(i for i in Transportation):
        result['data'][item.id] = item.to_dict(
            only=['id', 'departure', 'destination', 'order', 'driver', 'truck', 'status', 'value'])
    return result


@app.post('/transportation/save')
@db_session
def transportation_save():
    _id, data = Tool.get_post('status')
    if _id is not None:
        user = Transportation[_id]
        user.set(**data)
    else:
        Transportation(**data)


@app.post('/transportation/delete/:user_id')
@db_session
def transportation_delete(user_id):
    model = Transportation[int(user_id)]
    if model:
        model.delete()
        return {
            'result': 'success',
        }
    abort(400, 'Не найден пользователь')