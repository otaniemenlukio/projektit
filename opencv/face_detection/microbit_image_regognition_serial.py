'''
Test from Computer serial in MAC or linux,
1) find usb-device, type: ls /dev/cu.*
2) Name should look like: dev/cu.usbmodem1422
3) Type:screen /dev/cu.usbmodem1422 115200
4) To quit and exit terminal, write: ctrl+A and ctrl+D 
'''
from microbit import *
import neopixel

uart.init(baudrate = 115200)

num_of_pixels = 24
ledring = neopixel.NeoPixel(pin0, num_of_pixels)


def lights(red, green, blue):
    global ledring
    for i in range(24):
        ledring[i] = (red, green, blue)  # RGB -values
        sleep(50)
        ledring.show()

while True:
    message_bytes = uart.read()
    message = str(message_bytes)
    if "s" in message: #show on
        uart.write(b'Lights ON')
        lights(0, 0, 255)
        display.show(Image.HAPPY)
        sleep(5000)
        lights(0, 0, 0)
        display.show(Image.ASLEEP)
    elif "l" in message: #show off
        uart.write(b'Lights OFF')
        lights(0, 0, 0)
        display.show(Image.ASLEEP)
