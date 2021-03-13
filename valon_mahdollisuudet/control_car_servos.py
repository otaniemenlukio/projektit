from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

from drv8835 import DRV8835
#import control_servos
import input_handling
from servos import SERVOS

CAR = DRV8835()
CAR.stop()
SPEED = 60
TURNING_SPEED = 30

SERVOS = SERVOS()


def drive_forward():
    CAR.forward(SPEED, SPEED)
    


def drive_backward():
    CAR.backward(SPEED, SPEED)
    

# TODO: miten kääntyy sujuvasti vasemmalle/oikealle
def drive_left():
    CAR.forward(SPEED,TURNING_SPEED)

def drive_right():
    CAR.forward(TURNING_SPEED, SPEED)
    
# for testing    
def pan_right():
    current_angle = SERVOS.getServoAngle('pan')
    SERVOS.setServoAngle('pan',current_angle - 15 )

def pan_left():
    current_angle = SERVOS.getServoAngle('pan')
    SERVOS.setServoAngle('pan',current_angle + 15 )
    
def tilt_up():
    current_angle = SERVOS.getServoAngle('tilt')
    SERVOS.setServoAngle('tilt',current_angle + 15 )

def tilt_down():
    current_angle = SERVOS.getServoAngle('tilt')
    SERVOS.setServoAngle('tilt',current_angle - 15 )
# funktio, jota kutsutaan nappia painaessa

INPUT_MAP = {
    '\x1b[A' : drive_forward, # up arrow 
    '\x1b[B': drive_backward, # down arrow
    '\x1b[D': drive_left, 
    '\x1b[C': drive_right,
    '-': CAR.stop,
    'f': pan_right,
    's': pan_left,
    'e': tilt_up,
    'd': tilt_down,
    }

def main():
    orig_settings = input_handling.init()
    key = 0
    while key != 'q': # quit
        key = input_handling.get_input()
        if key == '\x1b': # Esc
            buf = key
            while True:
                key = input_handling.get_input()
                buf += key
                if key.isalpha(): # first letter
                    break
            if buf == '\x1b[A' or'\x1b[B' or'\x1b[C' or 'x1b[D': #arrow keys
                key = buf
        if key in INPUT_MAP:
            INPUT_MAP[key]()
        print("You pressed", key)
        
    SERVOS.stopServos()   
    input_handling.exit(orig_settings)
main()