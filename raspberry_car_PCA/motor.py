import curses, sys, os 
#Servo controller connected to IC2
import Adafruit_PCA9685
pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)

from time import sleep


#ESC Brushles motor states: direction, on/off
toggleState = 400
throttle = 450
delta = 20
print("toggleState1")
pwm.set_pwm(2,0,toggleState)
sleep(0.2)
for i in range(1,6):
    pwm_value = throttle -i*delta
    if pwm_value < toggleState:
        pwm.set_pwm(2,0,toggleState)
        sleep(0.2)
    pwm.set_pwm(2,0, pwm_value)
    sleep(0.4)
    print(pwm_value)
pwm.set_pwm(2,0,toggleState)
