# Feather Transistori Moottori
Tässä projektissa tehdään tuuletin jota saa säädettyä potentiometrin avulla. Halutessaan projektiin voi myös lisätä puheohjaus toiminnon Rasperry Pi:n ja Google AIY voice kitin avulla. 

## Projektin feather osuus

### Tarvikkeet
- Transistori
- Hyppylankoja
- kytkentäalusta
- Feather M0 ja siihen USB-johto
- jonkin suuruinen vastus
- Potentiometri eli säätövastus
- Moottori ja siihen sopiva tuuletin

### Yleistä
Tarkista että tietokoneessasi kortti ja portti ovat asetettu oikein. Mene Arduino-sovelluksessa "työkalut" valikkoon ja valitse sieltä kortiksi "Adafruit Feather M0" ja portiksi "/dev/cu.usbmodem1420". 
Projektia tehdessä kannattaa kytkentäalustaan perustaa maadoitus- ja käyttöjänniterivit. Nämä rivit ovat yleensä pitkät poikittaiset rivit, jotka sijaitsevat kytkentäalustan reunoilla. Rivi joka on merkitty - merkillä maadoitetaan, eli kytketään Featherin GND porttiin. Rivi, joka on merkitty + merkillä kytketään käyttöjännitteeseen eli tässä tapauksessa Featherin USB porttiin. Näin jos jokin projektin komponentti täytyy maadoittaa tai kytkeä jännitteeseen, voi sen yhdistää jompaankumpaan näistä riveistä 

### Potentiometrin kytkentä
Potentiometrissä on kolme pinniä. Keskimmäinen pinni kytketään Featherin analogiseen porttiin A2. Toinen jäljellejääneistä porteista kytketään käyttöjännitteeseen ja toinen maadoitetaan.

### Transistorin kytkentä
Transistorilla on kolme pinniä. Niistä keskimmäinen kytketään Featherin analogiseen porttiin A1. Oikeanpuolimmainen pinni kytketään toiseen moottorin porteista. Vasemmanpuolimmainen maadoitetaan. 

### Moottorin kytkentä
Moottorin toinen portti kytketään transistorin oikeanpuolimmaiseen pinniin ja toinen käyttöjännitteeseen.

![Kytkentäkaavio](Kytkentäkaavio_TransistoriMoottori.png)


### Ohjelmointi


>Ohjelman löydät kokonaisuudessaan tämän README.md tiedoston kanssa samasta kansiosta nimellä FeatherTransistoriMoottoriVer1.ino

```c++ 
#define MOOTTORI A1
#define POTENTIOMETRI A2
````
Määritämme missä porteissa moottori ja potentiometri sijaitsevat, tässä tapauksessa featherin analogisissa porteissa A1 ja A2.


```c++
void setup(){
    Serial.begin(9600);
}
````
Setup-funktiossa avaamme sarjamonitorin, jotta voimme myöhemmin tarkastella, toimiiko potentiometri halutulla tavalla.

```c++
void loop(){
    int potentiometri = analogRead(POTENTIOMETRI)/4;
    Serial.println(potentiometri);
    delay(100);
            
    analogWrite(MOOTTORI, potentiometri);
}
````
Feather toistaa loop-funktiota ikuisesti. Alussa luomme uuden kokonaisluku muotoisen (int) muuttujan nimeltä potentiometri. Annamme sille arvoksi analogRead-funktion avulla POTENTIOMETRI pinnin antaman arvon. Määritimme ohjelman alussa sen olevan featherin analogisen portin A2 arvo. Tämä arvo tulee vielä jakaa neljällä, koska analogRead-funktio antaa arvoja välillä 0-1023, mutta analogWrite ottaa arvoja väliltä 0-255.
Lopuksi käytämme analogWrite-funktiota, joka antaa sille ensimmäisenä parametrinä annetulle analogiselle portille toisena parametrina annetun arvon.



## Puheohjauksen lisääminen
Jos haluat, voit lisätä tuulettimelle puheohjaus ominaisuuden. Tässä osuudessa tarvitset Raspberryn ja Google Voice Kitin. 

### Ohjelmointi
#### Featherin osuus

```c++
#include <WiFi101.h>
#include <MQTTClient.h>
````
Jotta tuuletinta voi ohjata internetin välityksellä, pitää ottaa käyttöön WiFi ja MQTT-client eli välityspalvelinkirjasto.


```c++
#define MOOTTORI A1
#define POTENTIOMETRI A2


#define WIFI_NAME "12345678"
#define PASSWORD "asdfasdf"

char wifi_name[] = WIFI_NAME;
char password[] = PASSWORD;

WiFiClient wifi_client;
MQTTClient mqtt_client;

int status = WL_IDLE_STATUS;
````
Määritellään kytkentöjen pinnit ja Wifi-yhteyden tiedot.



```c++
void setup() {
  Serial.begin(9600);

  WiFi.setPins(8, 7, 4, 2);

  while(status != WL_CONNECTED) {
    Serial.print("Yhdistetään: ");
    Serial.println(wifi_name);

    status = WiFi.begin(wifi_name, password);
    delay(10000);
  }
  Serial.println("Yhdistetty Wifiin");

  mqtt_client.begin("broker.shiftr.io", wifi_client);
  
  while (!mqtt_client.connect("asdf", "aalto-shiftr-testi", "aalto-shiftr-testi")){
    Serial.println("Yhdistetään shiftriin");
    delay(1000);
  }
  Serial.println("Yhdistetty shiftriin");
  
  mqtt_client.onMessage(update);
  mqtt_client.subscribe("/tuuletin");
}
````
Ensin yhdistetään Wifiin ja välityspalvelimeen. Kuunnellaan tuuletinaiheisia viestejä välityspalvelimelta. 

```c++
void update(String &topic, String &message){
  Serial.println("Uusi viesti:");
  Serial.println(message);

  if(message == "full"){
    full_speed();
  }
  else if(message == "half"){
    half_speed();
  }
  else if(message == "off"){
    off();
  }
}
````
Määritellään funktio, joka ajetaan jos välityspalvelimelta saadaan tuuletinaiheinen viesti ja toimitaan sen mukaan. Eli, jos saadaan palvelimelta viesti "full", säädetään tuuletin täydelle teholle.

```c++

//Alla määritellään funktiot full_speed(), half_speed() ja off() joilla säädellään moottorin tilaa 
void full_speed(){
  analogWrite(MOOTTORI, 255);
}
void half_speed(){
  analogWrite(MOOTTORI, 128);
}
void off(){
  analogWrite(MOOTTORI, 0);
}
void loop() {
   mqtt_client.loop();
}
```
Määritellään funktiot jotka säätävät tuulettimet tietylle teholle.

#### Raspberryn osuus
Valmistele Google Voice Kit. Katso ohjeet:
[Linkki Ohjeisiin](https://github.com/otaniemenlukio/projektit/tree/master/RaspberryValmistelu)

```python
import iot

@iot.listen("it's too hot")
def full():
    iot.publish("komento_asdf","full")

@iot.listen("stop")
def off():
    iot.publish("komento_asdf","off")

@iot.listen("half speed")
def half():
    iot.publish("komento_asdf","half")

iot.run("puheohjaus", "aalto-shiftr-testi", "aalto-shiftr-testi")
```
Sisällytetään ohjelmaan iot-kirjasto. Kuunnellaan mitä Google Voice Kitille on sanottu iot.listen()-komennon avulla. Lopuksi käynnistetään iot-apuri, jossa määritellään shift käyttäjätunnus ja salasana.




