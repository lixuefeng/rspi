#coding=utf-8
from send_mail import *

def callCallbackFunc(call):
    text=u'''callId:{}\r type:{}\r number:{}\r '''.format(call.id, call.type, call.number)

    sendMail(text, subject=u'来电提醒')
    call.hangup()


def msgCallbackFunc(msg):
    text=u'''status:{}\r number:{}\r text:{}\r smsc:{}\r time:{}\r '''.format(msg.status, msg.number, msg.text, msg.smsc, msg.time)

    sendMail(text, subject=u'短信转发')
