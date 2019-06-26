# Microbit askelmittari
Microbitissä on kiihtyvyysanturi, jolla voi tunnistaa liikkeitä, esimerkiksi askelia. Tässä yksinkertaisessa projektissa microbitistä tehdään askelmittari, jonka voi laittaa vaikka taskuun. Nappia painamalla askelmäärän saa näkyviin


### Tarvikkeet 
- Microbit ja siihen USB-johto 
- Kaksi AAA paristoa ja sopiva liitäntä niille microbittiin

### Kytkentä

Kytke paristot microbitin yläosassa olevaan liittimeen. Muita kytkentöjä ei tarvita

### Ohjelma

Ohjelman voi tehdä koodilohkoilla tai pythonilla. Koodilohkot:
![Ohjelma](ohjelma.png)

Linkki ohjelmaan: https://makecode.microbit.org/_czV53zJs10PE

```python
from microbit import *
```
Otetaan käyttöön microbit-kirjasto
```python
askeleet = 0
```
Tehdään uusi muuttuja askeleet, johon varastoidaan askeleiden määrä.
```python
while True:
    if accelerometer.current_gesture() == "shake":
        askeleet += 1
        while accelerometer.current_gesture() == "shake":
            pass

    if button_a.is_pressed():
        display.scroll(askeleet)
```
Pääsilmukassa kuunnellaan A-napinpainalluksia ja ravistuksia. Jos microbit havaitsee ravistuksen, se lisää askeleet-muuttujaan yhden ja odottaa niin kauan, että yksittäinen ravistus eli askel päättyy. Jos nappia A painetaan, askeleiden määrä näytetään ledinäytöllä.
