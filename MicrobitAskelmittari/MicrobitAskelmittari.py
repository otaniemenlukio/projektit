from microbit import *


askeleet = 0

while True:
    if accelerometer.current_gesture() == "shake":
        askeleet += 1
        while accelerometer.current_gesture() == "shake":
            pass

    if button_a.is_pressed():
        display.scroll(askeleet)
