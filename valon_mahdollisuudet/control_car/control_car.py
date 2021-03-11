from drv8835 import DRV8835
import control_servos
import input_handling
import time

CAR = DRV8835()
CAR.stop()
SPEED = 60
TURNING_SPEED = 30


def drive_forward():
    CAR.forward(SPEED, SPEED)
    


def drive_backward():
    CAR.backward(SPEED, SPEED)
    

# TODO: miten kääntyy sujuvasti vasemmalle/oikealle
def drive_left():
    CAR.forward(TURNING_SPEED, SPEED)

def drive_right():
    CAR.forward(SPEED, TURNING_SPEED)
def do_nothing():
    print('give a command!')
# funktio, jota kutsutaan nappia painaessa
INPUT_MAP = {
    'i': drive_forward, 
    'k': drive_backward, 
    'j': drive_left, 
    'l': drive_right,
    'm': CAR.stop,
    }

def main():
    orig_settings = input_handling.init()
    key = 0
    while key != chr(27): # ESC
        key = input_handling.get_input()
        INPUT_MAP[key]()
        #print("You pressed", key)
        
        
    input_handling.exit(orig_settings)
main()