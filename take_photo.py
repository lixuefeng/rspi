#coding=utf-8
from send_mail import *
import os
os.system('raspistill -w 800 -h 600 -o test.jpg -ex backlight ')
#os.system('raspistill -w 800 -h 600 -t 60000 -tl 1000 -o image%04d.jpg')
#sendMultipartMail('test image', ['test.jpg'], subject=u'testimage')
