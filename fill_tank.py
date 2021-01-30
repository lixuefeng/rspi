import time
import RPi.GPIO as GPIO
pin=13
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin,GPIO.OUT)
def fill():
    GPIO.output(pin, 1)
    time.sleep(30)
    GPIO.output(pin, 0)
def check(frame):
    c = 0
    h,w,c = frame.shape
    p = frame.reshape(-1,).tolist()
    for i in range(0, len(p), 3):
        if p[i+2] > 170 and p[i+1] < 100 and p[i] < 100:
            c += 1
            x = i // 3 // w
            y = i // 3 % w
            frame[x][y][0] = 0
            frame[x][y][1] = 0
            frame[x][y][2] = 0
    print(c)
    return c > 300
def use_cv():
    import cv2
    while True:
        cap = cv2.VideoCapture(0)
        ret ,frame = cap.read()
        print(cap.get(0))
        if check(frame):
            fill()
            cv2.imwrite('data/img.{}.jpg'.format(time.time()), frame)
        cap.release()
        #time.sleep(3)
use_cv()
GPIO.cleanup()
