# coding: utf-8

import os, sys
reload(sys)
sys.setdefaultencoding('utf8')
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'site-packages.zip'))

import sae

from ifwechat.handlers.wechat import robot
from ifwechat.handlers.task import app

robot.config.from_pyfile('configs.py')

application = sae.create_wsgi_app(app)
