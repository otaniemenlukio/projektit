import paho.mqtt.client as mqtt
import time
import RPi.GPIO as GPIO
from drv8835 import DRV8835
import multiprocessing
import math

def to_signed(n):
    return n - ((0x80 & n) << 1)


def send_sensor_data(conn):
    mouse = open("/dev/input/mice", "rb")
    total_x = 0
    total_y = 0
    time_start = time.time()
    last_event_time = time_start
    while True:
        status, dx, dy = tuple(c for c in mouse.read(3))
        time_now = time.time()

        dx_dot = to_signed(dx)
        dy_dot = to_signed(dy)
        
        dx_mm = dx_dot*0.0254
        dy_mm = dy_dot*0.0254
        total_x += abs(dx_mm)
        total_y += abs(dy_mm)
        
        conn.send("{} {} {} {} {} {}".format(dx_mm, dy_mm, total_x, total_y, time_now-time_start, time_now-last_event_time))
        last_event_time = time_now
    
def car_control(conn):
    car = DRV8835() # if Pololulu Motoredriver is used
    car.stop()
    SPEED = 60
    LEFT = 1.0
    RIGHT = 1.0
    car.forward(LEFT * SPEED * 1.0, RIGHT * SPEED * 1.0)
    while True:
        message = conn.recv()
        dx_mm, dy_mm, total_x, total_y, elapsed, dt= map(float, message.split())
        if message == "END":
            break
        elif total_y >= 200: # Car is stopped when it moves 20 cm.
            car.stop()
        print("Vastaanotettu viesti {}, {}, {}, {}, {}, {}, {}, v_y={}".format(dx_mm, dy_mm, total_x, total_y, elapsed, dt, 1/dt,dy_mm/dt))

def on_connect(client, userdata, flags, rc):
    print("Yhdistettiin koodilla:", str(rc))
    client.subscribe("testing_raspbians")

def on_message(client, userdata, msg):
    command = str(msg.payload).lower()
    print(msg.topic, command)
    if command == "forward":# move forward
        print("Moving forward!")
        car.forward(LEFT * SPEED * 1.0, RIGHT * SPEED * 1.0)
        time.sleep(1)
        car.stop()
    elif  command == 'right':
        print("Turning right!")
        car.forward(LEFT * SPEED * 1.0, 0.0)
        time.sleep(1)
        car.stop()
    elif command == 'left':  # turn left
        print("Turning left!")
        car.forward(0.0, RIGHT * SPEED * 1.0)
        time.sleep(1)
        car.stop()
    elif command == 'backward': # move the car backwards
        print("Going backwards!")
        car.backward(LEFT * SPEED * 1.0, RIGHT * SPEED * 1.0)
        time.sleep(1)
        car.stop()
    elif command == 'circle':  # turn left
        print("Running in circles!")
        car.forward(LEFT * SPEED * 1.0, RIGHT * SPEED * 0.3)
        time.sleep(5)
        car.stop()
    elif command == 'stop':  # stop the car
        print("Stop!")
        car.stop()

def main():
    try:
        sensor_conn, car_control_conn = multiprocessing.Pipe()
    
        process1 = multiprocessing.Process(target = send_sensor_data, args = (sensor_conn,))
        process2 = multiprocessing.Process(target=car_control, args = (car_control_conn,))
        
        process1.start()
        process2.start()
        
        process1.join()
        process2.join()
       
    except KeyboardInterrupt:
        #car.stop()
        print("Ohjelman suoritus paattyy.")


if __name__ == "__main__":
    main()
