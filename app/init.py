# -*- coding: utf-8 -*-
"""
 Created by Fuoco on 05.04.2015 for intelligeman
"""
__author__ = 'Fuoco'
__credits__ = ["Fuoco"]
__license__ = "GPL"
__version__ = "0.0.1"
__email__ = "recyger@gmail.com"

from bottle import Bottle, static_file, abort, request, response, HTTP_CODES
import os
from db import db_session
from settings import config
import json

app = Bottle()

class Tool(object):
    ADMIN = 1
    MANAGER = 2
    WORKER = 3

    User = None

    @classmethod
    def authenticate(cls, func):
        @db_session
        def authenticate_and_call(*args, **kwargs):
            if cls.User is None:
                account = request.get_cookie('account', None, config['secret-key'])
                if account is None:
                    abort(401)
                cls.User = User[account['id']]
            return func(*args, **kwargs)
        return authenticate_and_call

    @classmethod
    def authorize(cls, role):
        def wrapper(func):
            def authorize_and_call(*args, **kwargs):
                if not cls.User.role.id == role:
                    abort(401)
                return func(*args, **kwargs)
            return authorize_and_call
        return wrapper

    @staticmethod
    def get_post(name, data=None):
        if data is None:
            data = request.json
        if name in data.keys():
            _id = None
            if 'id' in data[name].keys():
                try:
                    _id = int(data[name]['id'])
                except:
                    pass
                finally:
                    del data[name]['id']
            return (_id, data[name])
        return None

@app.error(400)
@app.error(401)
@app.error(404)
@app.error(412)
def error_handler(code):
    response.content_type = 'application/json'
    return json.dumps({
        'error': response.status_code,
        'msg': HTTP_CODES[response.status_code] if response.status_code in HTTP_CODES.keys() else 'Unknown error',
    })

@app.route('/content/<path:path>')
def content(path):
    if not os.path.exists(os.path.join('./content', path)):
        abort(404)
    return static_file(path, root='./content')
