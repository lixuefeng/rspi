#coding=utf-8
#from send_mail import *
import os
import RPi.GPIO as GPIO
import time
#pin=13
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(pin,GPIO.OUT)
#GPIO.output(pin, 1)
#time.sleep(120)
os.system('raspistill -w 640 -h 600 -o test.jpg -ex auto ')
#os.system('raspistill -w 480 -h 520 -t 120000 -tl 1000 -o image%03d.jpg')
#sendMultipartMail('test image', ['test.jpg'], subject=u'testimage')
#GPIO.output(pin, 0)
GPIO.cleanup()