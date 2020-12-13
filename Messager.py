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
    #modem.dial('17600958876')
    modem.Wait()
def deamonize():
    pid = os.fork()
    if pid:
        sys.exit(0)
    os.chdir('/home/pi')
    os.umask(0)
    os.setsid()
    sys.stdout.flush()
    sys.stderr.flush()
    with open('/dev/null') as read_null, open('/dev/null', 'w') as write_null:
        os.dup2(read_null.fileno(), sys.stdin.fileno())
        os.dup2(write_null.fileno(), sys.stdout.fileno())
        os.dup2(write_null.fileno(), sys.stderr.fileno())
    pid_file = '/home/pi/Messager_pid'
    if pid_file:
        with open(pid_file, 'w+') as f:
            f.write(str(os.getpid()))
        atexit.register(os.remove, pid_file)
if __name__ == '__main__':
    deamonize()

    from gsmmodem.modem import *
    powerOn()

