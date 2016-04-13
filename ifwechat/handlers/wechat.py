# coding: utf-8

import re, logging, socket
import werobot
from werobot.utils import to_binary
from ..utils import IfMaker, check_bind, add_event_task


robot = werobot.WeRoBot(enable_session=False)


@robot.subscribe
def subscribe(message):
    logging.info('user %s subscribe.' % (message.source,))
    return (u'欢迎使用IFMaker,在开始愉快的玩(zhe)耍(teng)前,您需要先绑定IFTTT Maker key.'
            u'\n发送 BD+{key} 绑定;'
            u'\n发送 help 获取帮助.')


@robot.unsubscribe
def unsubscribe(message):
    logging.info('user %s unsubscribe.' % (message.source,))
    id = to_binary(message.source)
    session_storage = robot.config["SESSION_STORAGE"]
    session_storage.delete(id)
    return ''


@robot.filter(re.compile(r'BD\+.+'))
def bind(message, session):
    key = message.content.lstrip('BD+').strip()
    ifmaker = IfMaker('ifmaker_test', key)
    try:
        code, _ = ifmaker.fetch(value1='test')
    except socket.timeout:
        return u'请求超时,请重试.'
    if code != 200:
        return u'您的输入有误,请绑定正确的key.'
    session['key'] = key
    logging.info('user %s bind %s' % (message.source, key))
    return u'绑定成功,重复绑定会覆盖以前的设置.'


@robot.filter('help')
def help(message):
    return u'<a href="https://github.com/zhu327/ifwechat/blob/master/README.md">查看帮助</a>'


@robot.text
@robot.voice
@check_bind
def text(message, session):
    if message.type == 'text':
        content = message.content.strip()
    elif message.type == 'voice':
        content = message.recognition.strip()
    if 'image' in session:
        image = session.pop('image')
        data = dict(value1=image, value2=content, key=session['key'])
        add_event_task('image', data)
        return u'您的[image]已进入消息队列,稍后会推送到IFTTT.'
    else:
        data = dict(value1=content, key=session['key'])
        add_event_task('text', data)
        return u'您的[text]已进入消息队列,稍后会推送到IFTTT.'


@robot.image
@check_bind
def image(message, session):
    session['image'] = message.img
    return u'您的照片已保存,请为照片配上一段文字.'


@robot.location
@check_bind
def location(message, session):
    data = dict(value1=message.label, value2=message.location[0],
                value3=message.location[1], key=session['key'])
    add_event_task('location', data)
    return u'您的[location]已进入消息队列,稍后会推送到IFTTT.'


@robot.link
@check_bind
def link(message, session):
    data = dict(value1=message.url, value2=message.title,
                value3=message.description, key=session['key'])
    add_event_task('link', data)
    return u'您的[link]已进入消息队列,稍后会推送到IFTTT.'
