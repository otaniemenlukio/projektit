from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#sudo pip3 install paho-mqtt
# Tai virtuaaliyparistossa pip install paho-mqtt

from drv8835 import DRV8835
#import control_servos
import input_handling
#import time

import paho.mqtt.client as mqtt # Tuodaan mqtt kirjasto
INSTANCE_NAME = "INSERT YOUR INSTANCE NAME"
PASSWD = "YOUR PASSWORD HERE"
RECEIV_CLIENT = "raspbCar" #vastaanottaja
TOPIC="car_commands"


CAR = DRV8835()
CAR.stop()
SPEED = 60
TURNING_SPEED = 30
# aseta pinnit
pan = 16
tilt = 26

GPIO.setup(tilt, GPIO.OUT) # vaaka => TILT
GPIO.setup(pan, GPIO.OUT) # pysty ==> PAN

pan_angle = 70
tilt_angle = 110

def setServoAngle(servo, angle):
	assert angle >=30 and angle <= 150
	pwm = GPIO.PWM(servo, 50)
	pwm.start(8)
	dutyCycle = angle / 18. + 3.
	pwm.ChangeDutyCycle(dutyCycle)
	sleep(0.3)
	pwm.stop()


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
def pan_servo_right():
    for i in range (30, 160, 15):
        setServoAngle(pan, i)
# funktio, jota kutsutaan nappia painaessa

INPUT_MAP = {
    '\x1b[A' : drive_forward, # up arrow 
    '\x1b[B': drive_backward, # down arrow
    '\x1b[D': drive_left, 
    '\x1b[C': drive_right,
    '-': CAR.stop,
    'f': pan_servo_right, #test servo
    'i' : drive_forward, # up arrow 
    'k': drive_backward, # down arrow
    'j': drive_left, 
    'l': drive_right,
    'm': CAR.stop,
    }

def on_connect(RECCEIV_CLIENT, userdata, flags, rc): # Funktio, joka pyöriteään aina, kun yhdistetään palvelimeen.
    print("Yhdistettiin koodilla:", str(rc)) # Tulostetaan koodi jolla ollaan yhditetty palvelimeen.
    client.subscribe(TOPIC) # Tilataan viesti kanava instance. Eli vastaanotetaan vain viestit, jotka tulevat tälle kanavalle.

def on_message(RECEIV_CLIENT, userdata, msg): # Funktio, joka pyöriteään aina, kun saadaa viesti.
    key = msg.payload.decode("utf-8")
    INPUT_MAP[key]()
    print(msg.payload.decode("utf-8")) # Tulostetaan viesti.


client = mqtt.Client(client_id = RECEIV_CLIENT) # Määritetään käyttäjä (client). Annetaan sille nimeksi "Kuuntelia".
client.on_connect = on_connect # Määritetään funktio, joka pyöritetään aina, kun yhdistetään palvelimeen.
client.on_message = on_message # Määritetään funktio, joka pyöritetään aina, kun saadaan viesti.
client.username_pw_set(INSTANCE_NAME, password = PASSWD) # Määritetään Avain sekä Salasana.
client.connect("controlcar.cloud.shiftr.io", 1883, 60) # Yhdistää shiftr.io:n palvelimelle. (ip, port, timeout)
client.loop_forever() # Pyöritetään ohjelmaa loputtomiin (siihen asti että sen itse lopetamme).


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
        
        
    input_handling.exit(orig_settings)


#main()