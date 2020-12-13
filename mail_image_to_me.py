#coding=utf-8
from send_mail import *
import os,sys
#os.system('raspistill -v -o test.jpg -w 640 -h 480 -t 30000 -tl 2000 -o image%04d.jpg')

sendMultipartMail('test image', sys.argv[1:], subject=u'testimage')
