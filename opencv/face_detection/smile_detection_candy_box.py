'''
Haar Cascade Face and Smile detection with OpenCV  

Developed by Marcelo Rovai - MJRoBot.org @ 22Feb2018
Editted mxheikki @20Oct2019

Face and smile regognition triggers serial communication with microbit and arduino.
If picamera doesnt work, try command: sudo modprobe bcm2835-v4l2

'''

import numpy as np
import cv2
import serial
import io

ser0 = serial.Serial('/dev/ttyACM0', timeout=1, baudrate=115200)
sio0 = io.TextIOWrapper(io.BufferedRWPair(ser0, ser0))

ser1 = serial.Serial('/dev/ttyACM1', timeout=1, baudrate=115200)
sio1 = io.TextIOWrapper(io.BufferedRWPair(ser1, ser1))

# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades
faceCascade = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')
smileCascade = cv2.CascadeClassifier('Cascades/haarcascade_smile.xml')
 
cap = cv2.VideoCapture(0)
cap.set(3,640) # set Width
cap.set(4,480) # set Height

while True:
    ret, img = cap.read()
    img = cv2.flip(img, -1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,      
        minSize=(30, 30)
    )

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
        smile = smileCascade.detectMultiScale(
            roi_gray,
            scaleFactor= 1.5,
            minNeighbors=15,
            minSize=(25, 25),
            )
        
        for (xx, yy, ww, hh) in smile:
            cv2.rectangle(roi_color, (xx, yy), (xx + ww, yy + hh), (0, 255, 0), 2)
            ser0.write(b'o') #oben the box
            ser1.write(b's') #smile microbit
               
        cv2.imshow('video', img)

    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        ser0.write(b'c')
        ser1.write(b'l')
        break

cap.release()
cv2.destroyAllWindows()