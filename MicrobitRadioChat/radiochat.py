import radio
from microbit import *

radio.on()

queue = []

wait_time = 200

letters_images = (
    Image("99999:"
          "90009:"
          "99999:"
          "90009:"
          "90009"),

    Image("99999:"
          "90009:"
          "99990:"
          "90009:"
          "99999"),

    Image("99999:"
          "90000:"
          "90000:"
          "90000:"
          "99999"),

    Image("99990:"
          "90009:"
          "90009:"
          "90009:"
          "99990"),

    Image("99999:"
          "90000:"
          "99990:"
          "90000:"
          "99999"),

    Image("99999:"
          "90000:"
          "99990:"
          "90000:"
          "90000"),

    Image("99999:"
          "90000:"
          "90099:"
          "90009:"
          "99999"),

    Image("90009:"
          "90009:"
          "99999:"
          "90009:"
          "90009"),

    Image("09990:"
          "00900:"
          "00900:"
          "00900:"
          "09990"),

    Image("00099:"
          "00009:"
          "00009:"
          "90009:"
          "99999"),

    Image("90009:"
          "90090:"
          "99900:"
          "90090:"
          "90009"),

    Image("90000:"
          "90000:"
          "90000:"
          "90000:"
          "99999"),

    Image("90009:"
          "99099:"
          "90909:"
          "90009:"
          "90009"),

    Image("90009:"
          "99009:"
          "90909:"
          "90099:"
          "90009"),

    Image("99999:"
          "90009:"
          "90009:"
          "90009:"
          "99999"),

    Image("99990:"
          "90009:"
          "99990:"
          "90000:"
          "90000"),

    Image("99999:"
          "90009:"
          "90009:"
          "99999:"
          "00090"),

    Image("99990:"
          "90009:"
          "99990:"
          "90009:"
          "90009"),

    Image("99999:"
          "90000:"
          "99999:"
          "00009:"
          "99999"),

    Image("99999:"
          "00900:"
          "00900:"
          "00900:"
          "00900"),

    Image("90009:"
          "90009:"
          "90009:"
          "90009:"
          "99999"),

    Image("90009:"
          "90009:"
          "09090:"
          "09090:"
          "00900"),

    Image("90009:"
          "90009:"
          "90909:"
          "90909:"
          "09090"),

    Image("90009:"
          "09090:"
          "00900:"
          "09090:"
          "90009"),

    Image("90009:"
          "90009:"
          "09090:"
          "00900:"
          "00900"),

    Image("99999:"
          "00090:"
          "00900:"
          "09000:"
          "99999"),

    Image("00900:"
          "99999:"
          "90009:"
          "99999:"
          "90009"),
    
    Image("09090:"
          "99999:"
          "90009:"
          "99999:"
          "90009"),

    Image("09090:"
          "99999:"
          "90009:"
          "90009:"
          "99999"),

    Image("00000:"
          "00000:"
          "00000:"
          "90009:"
          "99999:"),

    Image("00900:"
          "09000:"
          "99999:"
          "09000:"
          "00900:"),

    Image("00900:"
          "00090:"
          "99999:"
          "00090:"
          "00900:"),
     
)
def get_a_and_b():
    button_a.was_pressed()
    button_b.was_pressed()
    sleep(wait_time)
    return button_a.was_pressed(), button_b.was_pressed()

letters = "ABCDEFGHIJKLMNOPQRTSUVWXYZÅÄÖ br"
current_channel=7
radio.config(channel=current_channel)
def get_input():
    current_position = 0
    display.show(letters_images[current_position])
    msg=""
    while True:
        a, b = get_a_and_b()
        if a and b:
            if current_position == 30:
                msg=msg[:-1]
            elif current_position == 31:
                return msg
            else:
                msg+=letters[current_position]
        elif a and not b:
            current_position -= 1
            current_position%=len(letters)
            display.show(letters_images[current_position])
        elif not a and b:
            current_position += 1
            current_position%=len(letters)
            display.show(letters_images[current_position])

def update_inbox_screen():
    for i in range(25):
        if i < len(queue):
            display.set_pixel(i%5,i//5,9)
        else:
            display.set_pixel(i%5,i//5,0)
def set_one_pixel(position):
    for i in range(25):
    	if i == position:
            display.set_pixel(i%5, i//5, 9)
        else:
            display.set_pixel(i%5, i//5, 0)
def change_channel():
    global current_channel

    display.scroll("Channel:")
    for i in range(25):
        if i == current_channel:
            display.set_pixel(i%5, i//5, 9)
        else:
            display.set_pixel(i%5, i//5, 0)
    while True:
        a, b = get_a_and_b()
        if a and not b:
            current_channel -= 1
            current_channel %= 25
            
            set_one_pixel(current_channel)
        elif not a and b:
            current_channel += 1
            current_channel %= 25
                
            set_one_pixel(current_channel)
        elif a and b:
            radio.config(channel=current_channel)
            display.scroll("Set!")
            return
while True:
    a, b = get_a_and_b()
    if a and b:
        radio.send(get_input())
        display.scroll("Sent!")
        while button_a.is_pressed() or button_b.is_pressed():
            pass
    elif a and not b:
        if len(queue) != 0:
            display.scroll(queue.pop(0))
            update_inbox_screen()
        while button_a.is_pressed():
            pass
    elif not a and b:
        change_channel()
        update_inbox_screen()
    received = radio.receive()
    if received != None:
        queue.append(received)
        update_inbox_screen()

    
