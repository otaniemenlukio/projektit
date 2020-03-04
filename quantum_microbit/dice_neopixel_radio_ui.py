
# Write your code here :-)
from microbit import *
import neopixel
#import math
import time
import radio

radio.on()

num_pixels = 24
pixels = neopixel.NeoPixel(pin0, num_pixels)
#display.show(Image.HAPPY)
# Easy function for updating red , green, blue -values
def update_pixels(r, g, b):
    global pixels
    for i in range(24):
        pixels[i]=(r, g, b)
        sleep(10)
        pixels.show()
        


# wheel function
def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos*3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos*3)
        g = 0
        b = int(pos*3)
    else:
        pos -= 170
        r = 0
        g = int(pos*3)
        b = int(255 - pos*3)
    return (r, g, b)

# rainbow animation
def rainbow_cycle(wait):
    global num_pixels
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep_ms(wait)

# bounce animation
def bounce(r, g, b, wait):
    global pixels
    global num_pixels
    for i in range(2 * num_pixels):
        for j in range(num_pixels):
            pixels[j] = (r, g, b)
        if (i // num_pixels) % 2 == 0:
            pixels[i % num_pixels] = (0, 0, 0)
        else:
            pixels[num_pixels - 1 - (i % num_pixels)] = (0, 0, 0)
        pixels.show()
        time.sleep_ms(wait)

#cycle animation
def cycle(r, g, b, wait):
    global pixels
    global num_pixels
    for i in range(num_pixels):
        for j in range(num_pixels):
            pixels[j] = (0, 0, 0)
        pixels[i % num_pixels] = (r, g, b)
        pixels.show()
        time.sleep_ms(wait)

# Almost same as update pixels
def colorWipe(r, g, b, wait):
    global pixels
    global pixes
    for j in range(num_pixels):
        pixels[j] = (r, g, b)
        pixels.show()
        time.sleep_ms(wait)

# rainbow function goes through colors
def rainbow(wait):
    global num_pixels
    global pixels
    for j in range(255):
        for i in range(num_pixels):
            idx = int(i + j)
            pixels[i] = wheel(idx & 255)
            pixels.show()
        time.sleep_ms(wait)

def handle_message(message):
    if "1" in message:
        return 1
    elif "2" in message:
        return 2
    elif "3" in message:
        return 3
    elif "4" in message:
        return 4
    elif "5" in message:
        return 5
    elif "6" in message:
        return 6
    else:
        return 0
def show_result(number):
    global pixels
    #global num_pixels
    colorWipe(255, 0,0, 5)
    sleep(500)
    update_pixels(0, 0, 0)
    if number == 1:
        pixels[0] = (0, 0, 255)
        pixels.show()
    elif number == 2:
        pixels[0] = (0, 0, 255)
        pixels[12] = (0, 0, 255)
        pixels.show()
    elif number == 3:
        pixels[6] = (0, 0, 255)
        pixels[12] = (0, 0, 255)
        pixels[18] = (0, 0, 255)
        pixels.show()
    elif number == 4:
        pixels[0] = (0, 0, 255)
        pixels[6] = (0, 0, 255)
        pixels[12] = (0, 0, 255)
        pixels[18] = (0, 0, 255)
        pixels.show()
    elif number == 5:
        pixels[0] = (0, 0, 255)
        pixels[5] = (0, 0, 255)
        pixels[10] = (0, 0, 255)
        pixels[15] = (0, 0, 255)
        pixels[20] = (0, 0, 255)
        pixels.show()
    elif number == 6:
        pixels[0] = (0, 0, 255)
        pixels[4] = (0, 0, 255)
        pixels[8] = (0, 0, 255)
        pixels[12] = (0, 0, 255)
        pixels[16] = (0, 0, 255)
        pixels[20] = (0, 0, 255)
        pixels.show()
    sleep(2000)

#update_pixels(20,20,20)
waiting = False
got_answer = False

while True:
    if button_a.is_pressed():
        radio.send('start')
        waiting = True
        #colorWipe(255, 0,0, 10) # green
    if waiting:
        colorWipe(0, 255,0, 30) # green
        answer = handle_message(str(radio.receive()))
        sleep(500)
        update_pixels(0,0,0)
        if answer > 0:
            waiting = False
            got_answer = True
    
        else:
            pass
        
    if got_answer:
        #show_result(3)
        show_result(answer)
        got_answer = False
        pass

