# Processing
Processing on työkalu, jolla saa tuotettua helposti visuaalista tulostetta pelkän tekstin sijaan
## Asennus
Asennus onnistuu raspberrylle komennolla
```
curl https://processing.org/download/install-arm.sh | sudo sh
```
Osoitteesta https://processing.org/download/ voi ladata myös macille, linuxille ja windowsille.

Ota käyttöön python-tila oikeasta yläkulmasta: Add mode.. -> Python mode for Processing 3 -> Install
Samassa ikkunassa valitse välilehti Libraries. Etsi ja asenna MQTT, niin saat yhdistettyä shiftr:iin.

## Ensimmäinen ohjelma

```python
size(1024, 576)
line(100, 200, 400, 500)
```
Ohjelma luo ikkunan, jonka koko on 1024x576 ja piirtää suoran pisteestä (100, 200) pisteeseen (400, 500).

Viivan väriä saa vaihdettua funkiolla stroke ja paksuutta funktiolla strokeWeight
```python
stroke("#ff0000")           # Punainen hex
stroke(255, 0, 0)           # Punainen RGB

strokeWidth(30)             # 30px paksu
```
Nämä vaikuttavat kaikkiin tuleviin piirroksiin, jos niitä ei vaihdeta välissä. Esimerkiksi seuraava koodi piirtää kaksi punaista viivaa:
```python
stroke(255, 0, 0)
line(100, 100, 100, 200)
line(100, 100, 200, 100)
```

Muita piirtofunktioita:
```python
point(300, 100)             # piste (x, y) koordinaatteihin
circle(200, 200, 50)        # ympyrä, ensin x, y -koordinaatit, sitten säde
ellipse(200, 200, 100, 50)  # ellipsi, ensin x, y -koordinaatit, sitten leveys ja korkeus


fill(255, 0, 0)             # Ennen kuvioita voi käyttää funkioita fill ja noFill, jotka määräävät, täytetäänkö kuvio
noFill()                    # fill ottaa parametriksi värin, noFill nollaa kaiken, joten se ei tarvitse parametria

beginShape()                # piirtää monikulmion, jonka kulmat ovat pisteissä (300, 200), (300, 300) ja (400, 400)
vertex(300, 200)
vertex(300, 300)
vertex(400, 400)
endShape(CLOSE)

background(255, 255, 255)   # täyttää taustan värillä

```

## Shiftr:iin yhdistäminen

Shiftr:ia käyttäessä joudut käyttämään kiertotietä, koska kirjastoa ei suoraan tueta processingin python-moodissa. Kopioi seuraava koodinpätkä oman koodisi alkuun:
```python
add_library("mqtt")
class Adapter(MQTTListener):
    def messageReceived(topic, payload):
        pass
    def clientConnected(x):
        print("Connected")
    def connectionLost():
        print("Connection lost")
    def connect():
        clientConnected()
    def disconnect():
        connectLost()

adapter = Adapter()

client = MQTTClient(this, adapter)
```

Processing käyttää funkiota draw kuin looppina. Sen sisällä ole koodi toistetaan niin kauan kuin ohjelma suljetaan:
```python
def draw():
    print("Tämä toistetaan")
```
Jos käyttää draw-funktiota, muun koodin täytyy olla setup-funktion sisällä. Esimerkki:
```python
def setup():
    size(1000, 1000)
    fill(255, 0, 0)

    global x
    x = 0

def draw():
    global x
    background(255, 255, 255)
    circle(x, x, 10)

    x = x + 1
```
Draw-funktiolla voi tehdä animaatioita.


