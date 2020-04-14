# Input
Processingissa voi muokata taidetta. Tämä onnistuu draw-funktiolla ja muuttujilla mouseX ja mouseY. Ne ovat kokonaislukumuuttujia, jotka kertovat hiiren X- ja Y-koordinaatit:

```processing
void setup() {
  size(255, 255);
  stroke(255);
}

  

void draw() {
  background(204);
  line(mouseX-25, mouseY, mouseX+25, mouseY);
  line(mouseX, mouseY-25, mouseX, mouseY+25);
}

```

Tämä ohjelma luo ikkunan, jossa on hiirtä seuraava rasti. Draw-funktio suoritetaan toistuvasti.

```processing
void setup() {
  size(800, 800);
  stroke(255);
}

  

void draw() {
  background(204);
  for(int i=0;i<101;i++){
    line(i*8,0,mouseX,mouseY);
    line(0,i*8,mouseX,mouseY);
    line(i*8,800,mouseX,mouseY);
    line(800,i*8,mouseX,mouseY);
  }
}

```
![pyramidi](images/pyramidi.png)
Ohjelma luo "pyramidin", jonka huippu seuraa hiirtä.


```processing
void setup() {
  size(400, 400);
  background(0);
  stroke(255, 255, 255);
}

void draw() {
  if (mousePressed) {
    line(pmouseX, pmouseY, mouseX, mouseY);
  }
}
```
Tässä mousePressed on muuttuja, joka on tosi, kun hiirellä klikataan. pmouseX ja -Y ovat muuttujia, jotka kertovat hiiren sijainnin edellisessä framessa. Kun hiiren liikkeen yhdistää, saadaan yhtenäinen piirtojälki.
