# -*- coding: utf-8 -*-
"""
 Created by Fuoco on 05.04.2015 for intelligeman
"""
__author__ = 'Fuoco'
__credits__ = ["Fuoco"]
__license__ = "GPL"
__version__ = "0.0.1"
__email__ = "recyger@gmail.com"

from init import app, Tool, abort
from db import User, Role, db_session, select

@app.post('/user/list')
@Tool.authenticate
@Tool.authorize(Tool.ADMIN)
@db_session
def user_list():
    result = {
        'users': {},
        'roles': {},
    }
    for item in select(i for i in User):
        result['users'][item.id] = item.to_dict()
    for item in select(i for i in Role):
        result['roles'][item.id] = item.to_dict()
    return result

@app.post('/user/save')
@Tool.authenticate
@Tool.authorize(Tool.ADMIN)
@db_session
def user_save():
    data = Tool.get_post('user')
    user_id = None
    if 'id' in data.keys():
        user_id = int(data['id'])
        del data['id']
    if not user_id is None:
        user = User[user_id]
        user.set(**data)
    else:
        User(**data)

@app.post('/user/delete/:user_id')
@Tool.authenticate
@Tool.authorize(Tool.ADMIN)
@db_session
def user_delete(user_id):
    user = User[int(user_id)]
    if user:
        user.delete()
        return {
            'result': 'success',
        }
    abort(400, 'Не найден пользователь')