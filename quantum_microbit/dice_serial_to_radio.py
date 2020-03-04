
# Write your code here :-)
from microbit import *
#import neopixel
#import math
import time
import radio

uart.init(baudrate = 115200)
radio.on()

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

waiting = False
got_answer = False

while True:
    incoming = radio.receive()
    if incoming == 'start':
        uart.write(b'start')
        waiting = True
    if waiting:
        message_bytes = uart.read()
        answer = handle_message(str(message_bytes))
        if answer > 0:
            waiting = False
            got_answer = True
    
        else:
            pass
        
    if got_answer:
        #show_result(3)
        radio.send(str(answer))
        got_answer = False
        pass

