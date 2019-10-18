'''
OPENCV INSTALLATION GUIDE for Rasberry pi:
1.Install python3 pip
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

camera = picamera.PiCamera()
camera.vflip = True
camera.resolution = (640, 480)
rawCapture = picamera.array.PiRGBArray(camera)
time.sleep(0.5)

camera.capture(rawCapture, format="bgr")
image = rawCapture.array

#Convert Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Blur imager to reduce noise
blurred = cv2.GaussianBlur(gray, (9,9), 0)

#Perform canny edge-detection
edged = cv2.Canny(blurred, 50, 150)

#Perform Hough lines probalistic transform
lines = cv2.HoughLinesP(edged, 1, np.pi/180, 10, 80, 1)

if (lines != None):
    for x1, y1, x2, y2 in lines[0]:
        cv2.line(image, (x1,y1), (x2, y2), (0, 255,0), 2)
        
cv2.imshow("Test Camera", image)
cv2.waitKey(0)