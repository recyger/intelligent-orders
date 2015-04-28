# -*- coding: utf-8 -*-
"""
 Created by Fuoco on 05.04.2015 for intelligeman
"""
__author__ = 'Fuoco'
__credits__ = ["Fuoco"]
__license__ = "GPL"
__version__ = "0.0.1"
__email__ = "recyger@gmail.com"

from init import app, Tool
from db import Model, db_session, select, datetime

@app.post('/model/list')
@Tool.authenticate
@Tool.authorize(Tool.ADMIN)
@db_session
def model_list():
    data = []
    for model in select(m for m in Model):
        data.append({
            'name': model.name,
        })
    return {
        'data': data,
        'content': '/content/models.html?_t=%i' % (datetime.now() - datetime(1970, 1, 1)).total_seconds()
    }