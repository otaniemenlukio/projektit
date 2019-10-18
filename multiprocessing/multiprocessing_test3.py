import multiprocessing
import time
import math

def to_signed(n):
    return n - ((0x80 & n) << 1)

def sender(conn):
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
        #print("%#02x %d %d" %(status, dx, dy))
    

def receiver (conn):
    while True:
        message = conn.recv()
        dx_mm, dy_mm, total_x, total_y, elapsed, dt= map(float, message.split())
        if message == "END":
            break
        print("Vastaanotettu viesti {}, {}, {}, {}, {}, {}, {}, v_y={}".format(dx_mm, dy_mm, total_x, total_y, elapsed, dt, 1/dt,dy_mm/dt))
    
if __name__ == "__main__":
    
    messages = ["Terve", "Moikka", "Heippa", "END"]
    
    parent_conn, child_conn = multiprocessing.Pipe()
    
    process1 = multiprocessing.Process(target = sender, args = (parent_conn,))
    process2 = multiprocessing.Process(target=receiver, args = (child_conn,))
    
    process1.start()
    process2.start()
    
    process1.join()
    process1.join()
    
    