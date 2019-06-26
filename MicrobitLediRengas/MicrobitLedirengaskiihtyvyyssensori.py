from microbit import *
import neopixel
import math
num_of_pix = 24
pixels = neopixel.NeoPixel(pin0, num_of_pix)

def get_angle():
    values = accelerometer.get_values()
    if values[0]!=0:
        if values[0]>=0 and values[1]>=0:
            angle=360-math.atan(values[1]/values[0]*2)*180/math.pi
        elif values[0]>=0 and values[1]<0:
            angle=-math.atan(values[1]/values[0]*2)*180/math.pi
        else:
            angle=180-math.atan(values[1]/values[0]*2)*180/math.pi
    elif values[1]>0:
        angle=270.0
    else:
        angle=90.0
    angle=360-angle
    
    return angle
def normalisointialgoritmi(angle):
    return int((angle//15+6)%24)

while True:
    angle=get_angle()
    i=normalisointialgoritmi(angle)
    pixels.clear()
    pixels[i]=(255,255,255)
    pixels.show()


    
