import time
import RPi.GPIO as GPIO
import math
from drv8835 import DRV8835

# auton nopeus ja suunta
SPEED = 50

LEFT = 1.0
RIGHT = 0.9

CALIBRATION_CONSTANT = 0.0254

# kalibroidessa kuljettava matka (mm)
CALIBRATION_DISTANCE = 300
# kuljettava matka (mm)
DISTANCE = 1000

def to_signed(n):
    return n - ((0x80 & n) << 1)

def send_data(mouse, last_event_time, calibration_constant):    
    status, dx, dy = tuple(c for c in mouse.read(3))
    time_now = time.time()

    dx_dot = to_signed(dx)
    dy_dot = to_signed(dy)
    
    dx_mm = dx_dot*calibration_constant
    dy_mm = dy_dot*calibration_constant
    
    dt = time_now - last_event_time
    print("{} {} {}".format(dx_mm, dy_mm, dt))
    return dx_mm, dy_mm, dt
        
def drive_car(car, speed, left, right):
    car.forward(left * speed * 1.0, right * speed * 1.0)

def measure_distance(car, speed, left, right, distance, calibration_constant=CALIBRATION_CONSTANT):
    mouse = open("/dev/input/mice", "rb")
    
    start_time = time.time()
    last_event_time = start_time
    total_x, total_y, total = 0.0, 0.0, 0.0
    drive_car(car, SPEED, LEFT, RIGHT)
    print("Mittaus alkaa")
    try:
        while True:
            dx, dy, dt = send_data(mouse, last_event_time, calibration_constant)
            last_event_time += dt
            total_x += abs(dx)
            total_y += abs(dy)
            total += math.sqrt(dx**2 + dy**2)
            
            if total >= distance:
                car.stop()
                break
            else:
                continue
                #drive_car(car, SPEED, LEFT, RIGHT)
                
    except KeyboardInterrupt:
        car.stop()
    return total, total_x, total_y, time.time() - last_event_time

def calibrate(measured, actual):
    calibration_constant = actual/measured
    return calibration_constant
    

def main():
    # time.sleep(3)
    car = DRV8835()
    car.stop()
    print("Kalibroidaan")
    measured = measure_distance(car, SPEED, LEFT, RIGHT, CALIBRATION_DISTANCE)[0]
    actual = float(input("Syötä oikea ajettu matka (mm): \t"))
    calibration_constant = CALIBRATION_CONSTANT * calibrate(measured, actual)
    print("Calibration constant:", calibration_constant)
    input("Paina jatkaaksesi mittausta.")
    
    total, total_x, total_y, t = measure_distance(car, SPEED, LEFT, RIGHT, DISTANCE, calibration_constant)
    print(f"Ohjelma päättyy. Kuljettu matka: {total} mm, käytetty aika: {t} s")
    
    
if __name__ == "__main__":
    main()

