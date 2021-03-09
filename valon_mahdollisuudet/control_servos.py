#run aseta alkuarvot sudo python3 servoCtrl.py 70 110
from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#set pins
pan = 16
tilt = 26

GPIO.setup(tilt, GPIO.OUT) # pysty => TILT
GPIO.setup(pan, GPIO.OUT) # vaaka ==> PAN

def setServoAngle(servo, angle):
	assert angle >=30 and angle <= 150
	pwm = GPIO.PWM(servo, 50)
	pwm.start(8)
	dutyCycle = angle / 18. + 3.
	pwm.ChangeDutyCycle(dutyCycle)
	sleep(0.3)
	pwm.stop()

if __name__ == '__main__':
	import sys
	if len(sys.argv) == 1:
		setServoAngle(pan, 90)
		setServoAngle(tilt, 90)
	else:
		setServoAngle(pan, int(sys.argv[1])) # 30 ==> 90 (middle point) ==> 150
		setServoAngle(tilt, int(sys.argv[2])) # 30 ==> 90 (middle point) ==> 150
	GPIO.cleanup()
