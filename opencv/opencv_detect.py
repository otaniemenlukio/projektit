import picamera
import picamera.array
#import sys
import time
import cv2
import numpy as np
#import os

#Image processing parameters
KERNEL_SIZE = 9 #default value 15
LOW_THRESHOLD = 50 #default value 40
HIGH_THRESHOLD = 150 #default value 120

RHO = 10 #default 10
THRESHOLD = 10 #default 15
THETA = np.pi/180
MIN_LINE_LENGTH = 80 #default 10
MAX_LINE_GAP = 1


#Initialize camera
#video_capture = cv2.VideoCapture(0)
#time.sleep(0.2)

camera = picamera.PiCamera()
camera.vflip = True
camera.hflip = True
camera.resolution = (640, 480)



while True:
    rawCapture = picamera.array.PiRGBArray(camera)
    time.sleep(0.1)
    camera.capture(rawCapture, format="bgr")
    frame = rawCapture.array
    #ret, frame = video_capture.read()
    #time.sleep(0.1)
    
    #Convert to Grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #Blur image to reduce noise. The bigger the KERNEL_SIZE, more blurry the image
    blurred = cv2.GaussianBlur(gray, (KERNEL_SIZE, KERNEL_SIZE), 0)
    
    #Perform Canny edge-detection
    #If a pixel gradient higher than HIGH_THRESHOLD, it is considred as an edge
    #If a pixel gradient is lower tan LOW_THRESHOLD, it is not considered as an edge.
    #Recommended ratio HIGH : LOW is 3 :1
    edged = cv2.Canny(blurred, LOW_THRESHOLD, HIGH_THRESHOLD)
    
    #Hough lines  probablistic transformation
    lines = cv2.HoughLinesP(edged, RHO, THETA, THRESHOLD, MIN_LINE_LENGTH, MAX_LINE_GAP)
    
    # Draw Circles
    cv2.circle(frame, (320, 240), 20, (0,0,255), 1)
    cv2.circle(frame, (320, 240), 10, (0,255,0), 1)
    cv2.circle(frame, (320, 240), 2, (255,0,0), 2)
    
    #Grid drawn on the picture
    for y in range (0, 480, 40):
        cv2.line(frame, (0,y), (640, y), (255,0,0), 1)
        for x in range(0, 640, 40):
            cv2.line(frame, (x,0), (x, 480), (255,0,0),1)
    
    #Draw lines
    if lines != None:
        for x1,y1, x2,y2 in lines[0]:
            cv2.line(frame, (x1,y1), (x2,y2), (0,255,0),2)
            cv2.putText(frame, 'Lines detected', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255,0),1)
            print('x1:', x1, 'y1:', y1, 'x2: ', x2, 'y2:', y2)
    cv2.imshow('Line Test', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'): # waitKey(delay)
        break

#video_capture.release()
#cv2.destroyAllWindows()
