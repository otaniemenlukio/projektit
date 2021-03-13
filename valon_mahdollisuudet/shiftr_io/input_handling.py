import tty
import sys
import termios


def init():
    orig_settings = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin)
    return orig_settings

def get_input():
    return sys.stdin.read(1)

def exit(orig_settings):
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings) 



if __name__ == "__main__":
    settings = init()
    key = 0
    while key != chr(27): # esc
        key = get_input()
        print("'" + str(key) + "'")
    exit(settings)