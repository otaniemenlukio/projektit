from drv8835 import DRV8835
from time import sleep

car = DRV8835()

car.stop()
SPEED = 60
LEFT = 1.0
RIGHT = 1.0
car.forward(LEFT * SPEED * 1.0, RIGHT * SPEED * 1.0)
sleep(2.0)
car.stop()