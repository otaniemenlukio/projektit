import picamera
import picamera.array
import time
import cv2

camera = picamera.PiCamera()
camera.vflip = True
camera.resolution = (640, 480)
rawCapture = picamera.array.PiRGBArray(camera)
time.sleep(0.5)

camera.capture(rawCapture, format="bgr")
image = rawCapture.array

cv2.imshow("Image Test", image)
cv2.waitKey(0)