from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# aseta pinnit
pan = 26
tilt = 16

GPIO.setup(tilt, GPIO.OUT) # vaaka => TILT
GPIO.setup(pan, GPIO.OUT) # pysty ==> PAN

def setServoAngle(servo, angle):
	assert angle >=30 and angle <= 150
	pwm = GPIO.PWM(servo, 50)
	pwm.start(8)
	dutyCycle = angle / 18. + 3.
	pwm.ChangeDutyCycle(dutyCycle)
	sleep(0.3)
	pwm.stop()
	

if __name__ == '__main__':  
    for i in range (30, 160, 15):
        setServoAngle(pan, i)
        setServoAngle(tilt, i)
    
    for i in range (150, 30, -15):
        setServoAngle(pan, i)
        setServoAngle(tilt, i)
        
    setServoAngle(pan, 100)
    setServoAngle(tilt, 90)    
    GPIO.cleanup()