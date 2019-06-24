from microbit import *
import neopixel
import time

num_pixels = 24
pixels = neopixel.NeoPixel(pin0, num_pixels)
current_pixel = 0

while True:
    if button_a.is_pressed():
        current_pixel-=1
        current_pixel=current_pixel%24
        for i in range(24):
            pixels[i]=(0,0,0)
        pixels[current_pixel]=(255,0,0)
        pixels.show()
        while button_a.is_pressed():
            pass

    if button_b.is_pressed():
        current_pixel+=1
        current_pixel=current_pixel%24
        for i in range(24):
            pixels[i]=(0,0,0)
        pixels[current_pixel]=(0,255,0)
        pixels.show()
        while button_b.is_pressed():
            pass