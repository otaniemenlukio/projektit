# Microbit radio chat
Tässä projektissa tehdään microbiteistä keskustelulaitteita, joilla voi lähettää viestejä muille microbiteille. Niissä on radiomoduuli, joilla ne voivat kommunikoida lähietäisyydellä olevien laitteiden kanssa.


### Tarvikkeet
- Microbit

Tässä projektissa tarvitaan vain microbitiä ja tietokonetta, jolla se ohjelmoidaan, mutta itse ohjelma on melko pitkä ja monimutkainen. Tässä ohjekokoelmassa on helpompiakin radiota käyttäviä projekteja.


```python3
import radio
from microbit import *

radio.on()

queue = []

wait_time = 200

letters = "ABCDEFGHIJKLMNOPQRTSUVWXYZÅÄÖ br"
current_channel=7
radio.config(channel=current_channel)

```
Käytetään radiokirjastoa ja microbitin perusfunktioita. Käynnistetään radio, määritellään jonomuuttuja ja muuttuja, joka määrittelee, kuinka kauan ohjelma odottaa napinpainallusta. Tehdään myös lista valikon eri vaihtoehdoista ja määritellään käytettävä kanava.

```python
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

...

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
```
Tehdään lista kuvista tekstinsyöttöä varten. Tässä ei ole koko listaa, mutta ohjelmassa on.
```python
def get_a_and_b():
    button_a.was_pressed()
    button_b.was_pressed()
    sleep(wait_time)
    return button_a.was_pressed(), button_b.was_pressed()

```
Tehdään fünktio, joka kokeilee, painettiinko nappeja. 
```python
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
```
Määritellään funktio, joka kysyy käyttäjältä merkkijonon.
```python
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
```
Ensimmäinen funktio näyttää jonon pituuden näytöllä ja toinen laittaa yhden ledin päälle ja sammuttaa loput.
```python
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
```
Funktio, joka näyttää valikon kanavan vaihtamista varten.
```python
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
```
Pääsilmukka
