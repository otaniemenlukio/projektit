#sudo pip3 install paho-mqtt

import input_handling

import paho.mqtt.client as mqtt # Tuodaan mqtt kirjasto
INSTANCE_NAME = "INSERT YOUR INSTANCE NAME"
PASSWD = "INSERT YOUR PASSWORD HERE"
SEND_CLIENT = "Sender" # Kysyy lahettajan nimen ja tallettaa sen muuttujaan.
TOPIC= "car_commands"
#MESSAGE = input("\nViesti:\n") # Kysyy viestin ja tallettaa sen muuttujaan.

client = mqtt.Client(client_id = SEND_CLIENT) # Määritetään käyttäjäksi (Client) nimi muuttja.
client.username_pw_set(INSTANCE_NAME, PASSWD) # Määritetään INSTANCE sekä Salasana.
client.connect("controlcar.cloud.shiftr.io", 1883, 3) # Yhdistää shiftr.io:n palvelimelle. (ip, port, timeout)
client.loop_start()
#client.publish(TOPIC, payload = (SEND_CLIENT + " : " + MESSAGE)) # Lähetetään viesti.
#client.publish(TOPIC, payload = MESSAGE)


def main():
    orig_settings = input_handling.init()
    key = 0
    while key != 'q': # quit
        key = input_handling.get_input()
        if key == '\x1b': # Esc
            buf = key
            while True:
                key = input_handling.get_input()
                buf += key
                if key.isalpha(): # first letter
                    break
            if buf == '\x1b[A' or'\x1b[B' or'\x1b[C' or 'x1b[D': #arrow keys
                key = buf
        client.publish(TOPIC, payload = key)
        print("You pressed", key)
        
        
    input_handling.exit(orig_settings)
main()