#coding=utf-8
import RPi.GPIO as GPIO
import sys
import signal
import time
import os
import atexit

GPIO.setmode(GPIO.BOARD)


def exit(signum, frame):
    GPIO.output(pin, GPIO.LOW)
    GPIO.cleanup()
    sys.exit(1)

def on_switch_pressed(channel):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(40)
    GPIO.output(pin, GPIO.LOW)

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
    pid_file = '/home/pi/Pumper'
    if pid_file:
        with open(pid_file, 'w+') as f:
            f.write(str(os.getpid()))
        atexit.register(os.remove, pid_file)
if __name__ == '__main__':
    #deamonize()

    signal.signal(signal.SIGINT, exit)

    pin=13
    GPIO.setup(pin,GPIO.OUT, initial=GPIO.LOW)
    on_switch_pressed(0)
    exit(0)

    channel=15
    GPIO.setup(channel, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    try:
        GPIO.add_event_detect(channel, GPIO.RISING, bouncetime = 200)
        while True:
            if GPIO.event_detected(channel):
                GPIO.remove_event_detect(channel)
                on_switch_pressed(channel)
                GPIO.add_event_detect(channel, GPIO.RISING, bouncetime = 200)
            time.sleep(0.5)     # 10毫秒的检测间隔
    except Exception as e:
        print(e)
    GPIO.cleanup()
