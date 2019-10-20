'''
Installation Guide:
1.Install python pip if necessary
wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py

2. Updates and prerequisites: 
sudo apt-get update
sudo apt-get install libhdf5-dev libhdf5-serial-dev
sudo apt-get install libqtwebkit4 libqt4-test
sudo apt-get install libatlas-base-dev libjasper-dev libqtgui4 python3-pyqt5

3. installation:
sudo pip install opencv-contrib-python

4. start Python and test:
import cv2
cv2.__version__

'''
import picamera
import picamera.array
import time
import cv2
import numpy as np
from drv8835 import DRV8835


#Image processing parameters
KERNEL_SIZE = 9 #default value 15
LOW_THRESHOLD = 50 #default value 40
HIGH_THRESHOLD = 150 #default value 120

RHO = 10 #default 10
THRESHOLD = 10 #default 15
THETA = np.pi/180
MIN_LINE_LENGTH = 80 #default 10
MAX_LINE_GAP = 1


camera = picamera.PiCamera()
camera.vflip = True # Depending how picamera installed on the car
camera.hflip = True
camera.resolution = (640, 480)


car = DRV8835() # if Pololulu Motoredriver is used
car.stop()
SPEED = 45
LEFT = 1.0
RIGHT = 1.0


while True:
    rawCapture = picamera.array.PiRGBArray(camera)
    time.sleep(0.1)
    camera.capture(rawCapture, format="bgr")
    frame = rawCapture.array
    
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
    
    #Draw lines and control car if lines detected in center of image frame.
    if lines != None:
        car.forward(LEFT * SPEED * 1.0, RIGHT * SPEED * 1.0)
        for x1,y1, x2,y2 in lines[0]:
            cv2.line(frame, (x1,y1), (x2,y2), (0,255,0),2)
            cv2.putText(frame, 'Lines detected', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255,0),1)
            if (x1 < 320 - 3*40 or x2 < 320 - 3*40) and ( y1 > 240 -3*40 and y1 < 240 + 3*40):
                car.forward(LEFT * SPEED * 0.8, RIGHT * SPEED * 1.0)
                print('x1: ', x1, 'y1:', y1)
                
            elif (x2 > 320 +3*40 or x1 > 320 +3*40) and (y2 > 240 - 3*40 and y2 < 240 + 3*40):
                car.forward(LEFT * SPEED * 1.0, RIGHT * SPEED * 0.8)
                print('x2: ', x2, 'y2: ', y2)
            else:
                print('x1:', x1, 'y1:', y1, 'x2: ', x2, 'y2:', y2 )
                
    cv2.imshow('Line Test', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'): # waitKey(delay)
        car.stop()
        break
    
