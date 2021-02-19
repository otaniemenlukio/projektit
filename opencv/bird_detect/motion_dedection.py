import cv2
#import imutils
import numpy as np
import math
import requests
import time

# Telegram settings:
BOT_API_TOKEN = 'INSERT YOUR TOKEN'
GROUP_ID = 'INSERT YOUR G-ID'
TG_URL = 'https://api.telegram.org/bot'+ BOT_API_TOKEN

def send_to_telegram(filename, type):
    """ Funktio lahettaa telegramiin tyypista riippuen 
        kuvan tai videon. """
    with open(filename, 'rb') as capture_file:
        if type == 'photo':
            url = TG_URL + '/sendPhoto'
            files = {"photo": capture_file}
        elif type == 'video':
            url = TG_URL + '/sendVideo'
            files = {"video": capture_file}
        res = requests.post(url, files=files, params={'chat_id': GROUP_ID})



cap = cv2.VideoCapture(0)
kernel = np.ones((3, 3), np.uint8)
img0 =cv2.flip(cap.read()[1],-1)
img1 =cv2.flip(cap.read()[1],-1)

width = cap.get(3)
height = cap.get(4)

#set dedect Range and Image parameters
dedectRange = 80 #distance of action center of the image
numImages = 5 # when this limit reached the program will stop
duration = 10 #duration of video capture

print('Image dimensions: ',width,height)
i = 0

def record_video():
    fourcc = cv2.VideoWriter_fourcc(*'FMP4') # FMP4 or XVID
    out = cv2.VideoWriter('output.mp4',fourcc, 20.0, (640,480)) #.avi
    start_time = time.time()
    while(time.time() - start_time < duration):
        ret, frame = cap.read()
        if ret==True:
            frame = cv2.flip(frame,-1)

            # write the flipped frame
            out.write(frame)
    
while(True):
    diffrence=cv2.absdiff(img1, img0)
    grey = cv2.cvtColor(diffrence, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grey, (3, 3), 0)
    ret, th = cv2.threshold( blur, 15, 255,
                             cv2.THRESH_BINARY)
    dilated = cv2.dilate(th, kernel, iterations=2)
    contours, hierarchy = cv2.findContours(dilated,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
    img2 = img0
    cv2.drawContours(img2, contours, -1, (0, 255, 0), 2)
    
    if len(contours)>0:
        for contour in contours:
            x, y, _, _ = cv2.boundingRect(contour)
            perimeter = cv2.arcLength(contour,True)
            print(x, " ", y, "perimeter: ", perimeter)
            if math.sqrt((x-width/2)**2+(y-height/2)**2)<dedectRange and perimeter > 30:
                
                cv2.imwrite('bird'+str(i)+'.jpg',cv2.flip(img1,-1))
                url = TG_URL + '/sendMessage'
                telegram_message = 'bird'+str(i)+' was dedected in ('+str(x)+', '+str(y)+')!'
                res = requests.post(url, params={'chat_id': GROUP_ID}, data ={'text': telegram_message})
                send_to_telegram('bird'+str(i)+'.jpg','photo')
                
                record_video()
                send_to_telegram('output.mp4','video')
                i = i+1
    
    
    
    cv2.imshow('Output', cv2.flip(img2,-1))
    img0=img1
    
    
    img1=cap.read()[1]
    if i> numImages:
        break
    
    if cv2.waitKey(5) == 27 :
        break

cv2.destroyAllWindows()
cap.release()