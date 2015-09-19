# encoding: utf-8

import urllib2, json, logging
from sae.taskqueue import add_task


MAKER_URL = 'https://maker.ifttt.com/trigger/{event}/with/key/{key}'


def check_bind(func):
    def wapper(message, session):
        if not 'key' in session:
            return (u'您还没有绑定IFTTT Maker key.'
                    u'\n发送 BD+{key} 绑定;'
                    u'\n发送 help 获取帮助.')
        return func(message, session)
    return wapper


def add_event_task(event, data):
    uri = '/task/{event}/'.format(event=event)
    logging.debug('add %s task %s' % (event, data))
    return add_task('queue', uri, json.dumps(data))


class IfMaker(object):
    def __init__(self, event, key):
        self.url = MAKER_URL.format(event=event, key=key)

    def fetch(self, **data):
        request = urllib2.Request(self.url)
        request.add_header('Content-type', 'application/json')
        request.add_data(json.dumps(data))
        try:
            response = urllib2.urlopen(request)
            code, content = response.getcode(), response.read()
        except urllib2.HTTPError as e:
            code, content = e.code, e.read()
            logging.error('ifttt url %s fetch error %s, %s' % (self.url, code, content))
        return code, content
