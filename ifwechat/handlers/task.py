# coding: utf-8

import json
from bottle import request, response
from wechat import robot
from ..utils import IfMaker

app = robot.wsgi

@app.post('/task/<event>/')
def task(event):
    b = request._get_body_string()
    data = json.loads(b)
    ifmaker = IfMaker(event, data.pop('key'))
    code, content = ifmaker.fetch(**data)
    response.status = code
    return content
