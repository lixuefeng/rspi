#coding=utf-8
import RPi.GPIO as GPIO
import time
pin=13
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin,GPIO.OUT)
GPIO.output(pin, 1)
time.sleep(30)
GPIO.output(pin, 0)
GPIO.cleanup()
