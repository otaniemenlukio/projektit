## Levynkuvan lataaminen ja poltto
1. Lataa levynkuva osoitteesta https://github.com/google/aiyprojects-raspbian/releases ja valitse uusin
2. Polta kuva SD-kortille esimerkiksi Etcherillä tai dd:llä

## Raspberryn käynnistys
1. Kytke hdmi-kaapeli, näppäimistö, hiiri ja virtalähde ja odota, kunnes raspberry käynnistyy
2. Ensimmäisen käynnistyksen jälkeen tulee ikkuna, jolla voi valita olennaisia asetuksia. Valitse ensimmäisessä näkymässä Next
3. Jos haluat kieleksi englannin, valitse sijainniksi United Kingdom ja kieleksi British English. Jos haluat suomen, valitse sijainniksi Finland ja kieleksi Finnish.
4. Poista valinta kohdasta "Use US keyboard" ja paina Next
5. Valitse Next ilman, että vaihdat salasanaa
6. Yhdistä wifiin
7. Hyväksy ohjelmistopäivitys ja odota sen valmistuminen
8. Kun päivitys on valmis, valitse ok ja reboot.
9. Vaihda näppäimistöasettelu ja aikavyöhyke:

Varmista, että ainakin seuraavat ovat valittuina:


![](https://raw.githubusercontent.com/Samelikameli/python-aalto/master/guides/images/configuration.png)

![](https://raw.githubusercontent.com/Samelikameli/python-aalto/master/guides/images/interfaces.png)

![](https://raw.githubusercontent.com/Samelikameli/python-aalto/master/guides/images/localisation.png)

Aikavyöhykkeeksi Helsinki ja asetteluksi Finnish ja variantiksi Finnish.

## Asennus

1. Avaa terminaali näppäinyhdistelmällä Control+Alt+T
2. Asenna tarpeellisia python-kirjastoja komennoilla 
```
sudo pip3 install flask paho-mqtt SpeechRecognition google-speech picamera
sudo apt install libsox-fmt-mp3 sox
```
3. Lataa paketti projekteja raspberrylle:
```
git clone https://github.com/Pohjois-Tapiolan-lukio/raspberry_pi-projects.git
```

```
hostname -I
```
Saat ip-osoitteen, jolla voit yhdistää raspberryn terminaaliin omalta koneeltasi. Avaa omalla koneella terminaali, yhdistä samaan wifi-verkkoon kuin raspberry ja aja komento `ssh pi@192.168.43.238` niin, että korvaat tämän ip:n sillä, jonka sait ajamalla hostname-komennon. Salasana on raspberry.

## Google assistant
1. Mene sivulle https://console.cloud.google.com/ ja kirjaudu google-tunnuksella
2. Hyväksy ehdot
![](https://raw.githubusercontent.com/Samelikameli/python-aalto/master/guides/images/login.png)
3. Luo uusi projekti ja keksi sille nimi
![](https://raw.githubusercontent.com/Samelikameli/python-aalto/master/guides/images/createproject.png)
![](https://raw.githubusercontent.com/Samelikameli/python-aalto/master/guides/images/projectname.png)
4. Valitse sivupalkista Library
![](https://raw.githubusercontent.com/Samelikameli/python-aalto/master/guides/images/library.png)
5. Etsi google assistant, klikkaa siitä ja paina enable
![](https://raw.githubusercontent.com/Samelikameli/python-aalto/master/guides/images/assistant1.png)
![](https://raw.githubusercontent.com/Samelikameli/python-aalto/master/guides/images/assistant2.png)
6. Paina Create credentials
![](https://raw.githubusercontent.com/Samelikameli/python-aalto/master/guides/images/credentials1.png)
7. Täytä tiedot ja paina "What credentials do I need?"
![](https://raw.githubusercontent.com/Samelikameli/python-aalto/master/guides/images/credentials2.png)
8. Paina "Set up consent screen"
![](https://raw.githubusercontent.com/Samelikameli/python-aalto/master/guides/images/oauth.png)
9. Keksi nimi, scrollaa alas ja hyväksy
![](https://raw.githubusercontent.com/Samelikameli/python-aalto/master/guides/images/oauthname.png)
10. Ensimmäisellä välilehdellä paina refresh ja download
![](https://raw.githubusercontent.com/Samelikameli/python-aalto/master/guides/images/credentials3.png)
![](https://raw.githubusercontent.com/Samelikameli/python-aalto/master/guides/images/credentials4.png)
11. Kopioi ladattu client_id.json raspberryn kansioon /home/pi/ ja nimeä se uudelleen assistant.json:ksi
12. Siirry AIY-esimerkkikansioon komennolla `cd ~/AIY-projects-python`
13. Aja `src/examples/voice/assistant_grpc_demo.py`
14. Aukeaa kirjautumisikkuna. Kirjaudu google-tililläsi
15. Assistantin pitäisi toimia. Kokeile kysyä siltä jotain
