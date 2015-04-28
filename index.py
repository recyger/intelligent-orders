# -*- coding: utf-8 -*-
"""
 Created by Fuoco on 31.03.2015 for intelligeman
"""
__author__ = 'Fuoco'
__credits__ = ["Fuoco"]
__license__ = "GPL"
__version__ = "0.0.1"
__email__ = "recyger@gmail.com"

from bottle import run, static_file, debug
from app import app


@app.route('/')
@app.route('/index')
@app.route('/index.html')
def load_ui():
    return static_file('index.html', root='./content')

if __name__ == '__main__':
    debug(True)
    run(app, host='127.0.0.1', port=5000, reloader=True)