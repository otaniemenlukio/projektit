import time
import math


def to_signed(n):
    return n - ((0x80 & n) << 1)


def get_mouse_data(mouse):


    status, dx, dy = tuple(c for c in mouse.read(3))
    time_now = time.time()

    dx_dot = to_signed(dx)
    dy_dot = to_signed(dy)
    
    dx_mm = dx_dot*0.0254
    dy_mm = dy_dot*0.0254

    return dx_mm, dy_mm, time_now


def main():
    mouse = open("/dev/input/mice", "rb")
    total_x = 0
    total_y = 0
    time_start = time.time()
    last_event_time = time_start

    while True:
        dx, dy, time_now = get_mouse_data(mouse)

        total_x += abs(dx)
        total_y += abs(dy)

        print(f"{time_now - time_start}: Moved {dx} in x-direction and {dy} in y-direction.")


if __name__ == "__main__":
    main()