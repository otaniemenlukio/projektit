import multiprocessing
import time

def to_signed(n):
    return n - ((0x80 & n) << 1)

def sender(conn):
    mouse = open("/dev/input/mice", "rb")
    while True:
        status, dx, dy = tuple(c for c in mouse.read(3))

        dx = to_signed(dx)
        dy = to_signed(dy)
        conn.send("viesti {}, {},{}".format(status, dx, dy))
        


def receiver (conn):
    while True:
        message = conn.recv()
        if message == "END":
            break
        print("Vastaanotettu viesti {}".format(message))
    
if __name__ == "__main__":
    
    messages = ["Terve", "Moikka", "Heippa", "END"]
    
    parent_conn, child_conn = multiprocessing.Pipe()
    
    process1 = multiprocessing.Process(target = sender, args = (parent_conn,))
    process2 = multiprocessing.Process(target=receiver, args = (child_conn,))
    
    process1.start()
    process2.start()
    
    process1.join()
    process1.join()
    
    