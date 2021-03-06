# Microbit ledirengas
Tässä projektissa ohjelmoidaan microbitin kanssa tomivalle ledirenkaalle kaksi yksinkertaista toiminnallisuutta. Ensimmäinen osuus on ledirenkaan ledin liikuttaminen mictobitin nappien avulla. Toisessa osuudessa liikutetaan ledejä mikrobitin kiihtyvyyssensorilla.
### Tarvikkeet
- Microbit ledirengas (Zip Halo Kitronik)
- Kaksi AAA paristoa ja sopiva liitäntä niille ledirenkaaseen
- Microbit ja siihen USB-johto

### Ledirenkaan kytkentä
Kiinnitä ledirengas Microbittiin käyttäen viittä ruuvia kuvan osoittamalla tavalla.
![Valokuva](LedirengasKuva.jpg)
Muista liittää paristot ledirenkaaseen Kitronik-merkin yllä olevaan valkoiseen liitäntään.

```python
from microbit import *
import neopixel
import time

num_pixels = 24
pixels = neopixel.NeoPixel(pin0, num_pixels)
current_pixel = 0
````
Sisällytetään ohjelmaan tarvittavat kirjastot import-komennolla. Määritetään muuttujat num_pixel (ledirenkaan ledien määrä), pixels (luodaan ilmentymä NeoPixel-luokasta) ja current_pixel (ledi, joka sytytetään).

```python
while True:
    if button_a.is_pressed():
        current_pixel-=1
        current_pixel=current_pixel%24
        for i in range(24):
            pixels[i]=(0,0,0)
        pixels[current_pixel]=(255,0,0)
        pixels.show()
        while button_a.is_pressed():
            pass

    if button_b.is_pressed():
        current_pixel+=1
        current_pixel=current_pixel%24
        for i in range(24):
            pixels[i]=(0,0,0)
        pixels[current_pixel]=(0,255,0)
        pixels.show()
        while button_b.is_pressed():
            pass
````
While True-silmukkaa toistetaan ikuisuuden. Sen sisällä on kaksi if-käskyä, joiden avulla määritetää, mitä nappien painalluksessa tapahtuu. Jos nappia A painetaan, ledin paikka siirtyy yhden vasemmalle. Current_pixel-muuttujasta vähennetään yksi. Kun nappia B painetaan siirtyy ledi yhden oikealle, joten muuttujaan lisätään yksi. Jotta current_pixel-muuttujalle ei tulisi ikinä arvoa, joka on suurepi kuin 23 tai pienempi kuin nolla, seuraavalla rivillä sille annteaan arvoksi itsensä ja 24 jakojäännös. Tämä tehdään %-merkillä. Pixels on lista ledejä. For-silmukan sisällä asetamme ledit pois päältä. Sen jälkeen sytytämme listan jäsenen, joka on indeksillä current_pixel. Listan sisältö näytetään show()-funktiolla. Jos nappia vielä painetaan if-komennon suorituksen aikana, odotetaan sitä, että se päästetään vapaaksi while-silmukan avulla. 







[Koodi koodilohkoilla](https://makecode.microbit.org/_0s08bAE98Rdg)


```python
from microbit import *
import neopixel
import math
num_of_pix = 24
pixels = neopixel.NeoPixel(pin0, num_of_pix)
```
Otetaan kirjastot käyttöön ja luodaan pixels-olio.


```python
def get_angle():
    values = accelerometer.get_values()
    if values[0]!=0:
        if values[0]>=0 and values[1]>=0:
            angle=360-math.atan(values[1]/values[0]*2)*180/math.pi
        elif values[0]>=0 and values[1]<0:
            angle=-math.atan(values[1]/values[0]*2)*180/math.pi
        else:
            angle=180-math.atan(values[1]/values[0]*2)*180/math.pi
    elif values[1]>0:
        angle=270.0
    else:
        angle=90.0
    angle=360-angle
    
    return angle
def normalisointialgoritmi(angle):
    return int((angle//15+6)%24)
```
Määritellään funktiot, joiden avulla saadaan kallistussuunta, ja suunta muutettua ledien indekseiksi. Varsinkin kulmanlaskemisfunktio on melko sekava ja siinä käytetään trigonometriaa, joten sitä ei ole pakko ymmärtää.
```python
while True:
    angle=get_angle()
    i=normalisointialgoritmi(angle)
    pixels.clear()
    pixels[i]=(255,255,255)
    pixels.show()
```
Ohjelman pääsilmukassa laitetaan päälle se ledi, jota kohti microbitiä kallistetaan.
