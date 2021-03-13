#run aseta alkuarvot sudo python3 servoCtrl.py 70 110
from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class SERVOS():
    def __init__(self):
        #set pins
        self.pan = 16
        self.tilt = 26
        self.pan_angle = 110
        self.tilt_angle = 70

        GPIO.setup(self.tilt, GPIO.OUT) # pysty => TILT
        GPIO.setup(self.pan, GPIO.OUT) # vaaka ==> PAN
        
        self.setServoAngle('pan', self.pan_angle)
        self.setServoAngle('tilt', self.tilt_angle)

    def setServoAngle(self, servo, angle):
        #assert angle >=30 and angle <= 150
        if angle < 30:
            angle = 30
        if angle > 150:
            angle = 150
        if servo == 'pan':
            pwm = GPIO.PWM(self.pan, 50)
            self.pan_angle = angle
        else:
            pwm = GPIO.PWM(self.tilt, 50)
            self.tilt_angle = angle
        pwm.start(8)
        dutyCycle = angle / 18. + 3.
        pwm.ChangeDutyCycle(dutyCycle)
        sleep(0.3)
        pwm.stop()
    
    def getServoAngle(self, servo):
        if servo == 'pan':
            return self.pan_angle
        else:
            return self.tilt_angle

    
        
    def stopServos(self):
        GPIO.cleanup()
        
