# Microbit kompassi
Microbitin sisällä on kompassi, jonka ympärille voi rakentaa mielenkiintoisia ohjelmia. Tässä projektissa käytetään microbitin kanssa toimivaa ledirengasta näyttääkseen pohjoisen suunnan. 
### Tarvikkeet 
- Microbit ja siihen USB-johto 
- Microbit ledirengas (Zip Halo Kitronik)
- Kaksi AAA paristoa ja sopiva liitäntä niille ledirenkaaseen

```python
from microbit import *
import neopixel
import math

num_of_pix = 24
np = neopixel.NeoPixel(pin0, num_of_pix)
```
Otetaan käyttöön tarvittavat kirjastot ja alustetaan neopixel-ledirengas.
```python
while True:
    angle = compass.heading()
    
    position = math.floor(23-angle//15)
    np.clear()
    np[position]=(0,255,0)

    np.show()
```
Ohjelman pääsilmukassa luetaan kulma ja tallennetaan se muuttujaan. Muutetaan asteluku ledin paikaksi jakamalla luvulla 15, koska 360/24=15. Silmukan lopuksi näytetään vihreä ledi halutussa kohdassa.
[Ohjelma koodilohkoina](https://makecode.microbit.org/08388-48868-67546-29893)
