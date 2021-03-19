import curses, sys, os, time 
#Servo controller connected to IC2
import Adafruit_PCA9685
pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)
from time import sleep

#ESC Brushles motor states: direction, on/off
toggleState = 400
init_throttle = 430
delta_throttle = 20
driving = False
if init_throttle > toggleState:
    dir = 1
else:
    dir =-1


#max values for throttle:
fwdmax = 600
revmin = 200


#steering pwm values for Servo
steering_center = 370
steering_max_left = 530
steering_min_right = 210
delta_steering = 20

#control values for servo and esc
throttle_pwm = init_throttle
steering_pwm = steering_center

#user interface
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

def printscreen():
        # The command os.system('clear') clears the screen.
        os.system('clear')
        print("============ RC car controller ============\r")
        print(u"\u2191/\u2193: accelerate/brake\r")
        print(u"\u2190/\u2192: left/right\r")
        print("q:   stops the motor and exit\r")
        print("x:   exit the program\r")
        print("s:   start the program\r")
        

while True:
    printscreen()
    char = screen.getch()
    
    if char == ord('q'):
        pwm.set_pwm(2, 0, toggleState)
        pwm.set_pwm(1, 0, steering_center)

        break
    elif char == ord('-'):
        steering_pwm = steering_center
        print('center steering')
    
    elif char == ord('s'):
        print("lets start driving!")
        driving = True
        pwm.set_pwm(2,0,toggleState)
        sleep(0.1)
    elif char == curses.KEY_UP:
        print('forward')
        if throttle_pwm == init_throttle and not driving:
            time.sleep(0.2)
            continue
        elif throttle_pwm + delta_throttle < fwdmax:
            throttle_pwm += delta_throttle
            if throttle_pwm > toggleState and dir < 0:
                pwm.set_pwm(2,0,toggleState)
                print('toggle1')
                dir = 1
                sleep(0.1)
                    
    elif char == curses.KEY_DOWN:
        print('reverse')
        if throttle_pwm == init_throttle and not driving:
            time.sleep(0.2)
            continue
        elif throttle_pwm +delta_throttle > revmin:
            throttle_pwm -= delta_throttle
            if throttle_pwm < toggleState and dir > 0:
                pwm.set_pwm(2,0,toggleState)
                print('toggle2')
                dir = -1
                sleep(0.1)
    
    elif char == curses.KEY_RIGHT:
        print('right')
        steering_pwm -= delta_steering
        if steering_pwm < steering_min_right:
            steering_pwm = steering_min_right                
    
    elif char == curses.KEY_LEFT:
        print('left')
        steering_pwm += delta_steering
        if steering_pwm > steering_max_left:
            steering_pwm = steering_min_left 
    
    printscreen()
    print(throttle_pwm)
    pwm.set_pwm(2, 0, throttle_pwm)
    pwm.set_pwm(1, 0, steering_pwm)
    sleep(0.2)
    
curses.nocbreak(); screen.keypad(0); curses.echo()
curses.endwin()   
