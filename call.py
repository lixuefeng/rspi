#coding=utf-8
import sys
sys.path.append('.')
import time
import os
import atexit
from callbacks import *
def powerOn():
    modem = GsmModem('/dev/ttyUSB2',
                     incomingCallCallbackFunc=callCallbackFunc,
                     smsReceivedCallbackFunc=msgCallbackFunc)
    modem.connect()
    modem.processStoredSms()
    modem.dial('18001311238')
    modem.Wait()
if __name__ == '__main__':
    from gsmmodem.modem import *
    powerOn()

