# Erilaiset kuviot
Processingissa voi piirtää monenlaisia kuvioita, esimerkiksi pisteitä, viivoja ja ympyröitä.

Katsotaan tätä jo tuttua esimerkkikoodia. Siinä rivi `line(0, 0, 200, 200);` piirtää viivan.
Se on siis komento, jolle annetaan parametreja. Tässä ne ovat kahden pisteen koordinaatit.

```processing
void setup() {
  size(400, 400);
  stroke(255, 255, 255);
  line(0, 0, 200, 200);
}

void draw() {

}
```

Muita komentoja, joilla voi piirtää:

`ellipse(x, y, w, h);` Piirtää ellipsin, jonka keskipiste on koordinaateissa (x, y), leveys on w ja korkeus on h.
Esimerkiksi `ellipse(150, 200, 10, 20);` piirtää ellipsin, jonka keskipiste on koordinaateissa (150, 200),
on 10 pikseliä leveä ja 20 pikseliä korkea. Jos korkeus ja leveys on sama, syntyy ympyrä.

`point(300, 100);` Piirtää pisteen koordinaatteihin (300, 100)



Oletuksena muodot täytetään värillä. Sen voi kytkeä pois päältä noFill();

Takaisin täytön saa fill(255, 255, 255);


`stroke("#ff0000");`  Punainen hex
`stroke(255, 0, 0);`  Punainen RGB

`strokeWidth(30);`    30px paksu

Nämä vaikuttavat kaikkiin tuleviin piirroksiin, jos niitä ei vaihdeta välissä.
