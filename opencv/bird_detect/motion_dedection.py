import cv2
#import imutils
import numpy as np
import math
import requests


BOT_API_TOKEN = 'Token Here'
GROUP_ID = 'Group ID here'
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


k = np.ones((3, 3), np.uint8)
t0 =cv2.flip(cap.read()[1],-1)
t1 =cv2.flip(cap.read()[1],-1)

width = cap.get(3)
height = cap.get(4)
print(width,height)
i = 0
while(True):
    d=cv2.absdiff(t1, t0)
    grey = cv2.cvtColor(d, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grey, (3, 3), 0)
    ret, th = cv2.threshold( blur, 15, 255,
                             cv2.THRESH_BINARY)
    dilated = cv2.dilate(th, k, iterations=2)
    contours, hierarchy = cv2.findContours(dilated,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
    t2=t0
    cv2.drawContours(t2, contours, -1, (0, 255, 0), 2)
    
    if len(contours)>0:
        for contour in contours:
            x, y, _, _ = cv2.boundingRect(contour)
            print(x, " ", y)
            if math.sqrt((x-width/2)**2+(y-height/2)**2)<25:
                #print("Found")
                cv2.imwrite('bird'+str(i)+'.jpg',cv2.flip(t1,-1))
                i = i+1
                url = TG_URL + '/sendMessage'
                telegram_message = 'bird'+str(i)+' was dedected!'
                res = requests.post(url, params={'chat_id': GROUP_ID}, data ={'text': telegram_message})
                send_to_telegram('bird'+str(i)+'.jpg','photo')
                #if i>3:
                    #break
        print("next")
    
    
    
    
    cv2.imshow('Output', cv2.flip(t2,-1))
    t0=t1
    
    
    t1=cap.read()[1]
    if i>5:
        break
    
    if cv2.waitKey(5) == 27 :
        break

cv2.destroyAllWindows()
cap.release()
