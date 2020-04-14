# Ensimmäinen Processing -ohjelma

Testivaiheessa kokeiltiin tätä ohjelmaa:

```processing
void setup() {
  size(400, 400);
  stroke(255, 255, 255);
  line(0, 0, 200, 200);
}
      
void draw() {

}
```

Tässä ohjelmassa on kaksi funktiota, setup ja draw. Setup suoritetaan kerran ohjelman alussa. Draw suoritetaan toistuvasti koko ohjelman ajan. Koska tässä draw:n sisällä ei ole koodia, se ei tee mitään. Funktiot erotetaan muusta ohjelmasta hakasulkeilla {} ja jokainen komento päättyy puolipisteeseen ;

**Huomaa, että draw ei tässä liity piirtämiseen, vaan myös setupissa voi piirtää.**

Ohjelma luo ikkunan ja piirtää siihen yhden viivan:

Komento size(400, 400); luo ikkunan, jonka koko on 400px * 400px.

stroke(255, 255, 255); asettaa piirron väriksi valkoisen. Valkoisen RGB-arvo on (255, 255, 255) Väriä voi muuttaa monta kertaa ohjelman aikana. 

line(0, 0, 200, 200); piirtää viivan pisteestä (0, 0) pisteeseen (200, 200).

Lisäksi halutessaan voi muuttaa taustan väriä komennolla background. Esimerkiksi background(0, 0, 0); tekee taustasta mustan.

Kokeile muuttaa numeroarvoja ohjelmassa. Entä miten saat lisättyä kuvaan toisen viivan? Osaatko piirtää kolmella viivalla kolmion?
