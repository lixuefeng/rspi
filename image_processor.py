#coding=utf-8

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('test.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

plt.subplot(121)
plt.imshow(gray,'gray')
plt.xticks([])
plt.yticks([])
#cv2.namedWindow('imf',cv2.WINDOW_NORMAL)
#s=cv2.imshow('sss',img)
circles1 = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1, 10,param1=100,param2=30,minRadius=5,maxRadius=800)
circles = circles1[0,:,:]
circles = np.uint16(np.around(circles))
for i in circles[:]:
 cv2.circle(img,(i[0],i[1]),i[2],(0,0,255),2)
 cv2.circle(img,(i[0],i[1]),2,(0,0,255),2)
 #cv2.rectangle(img,(i[0]-i[2],i[1]+i[2]),(i[0]+i[2],i[1]-i[2]),(255,255,0),5)
#cv2.imshow('dd',s)

print("圆心坐标",i[0],i[1])
plt.subplot(122)
plt.imshow(img)
plt.xticks([])
plt.yticks([])
plt.savefig('fff.jpg')
