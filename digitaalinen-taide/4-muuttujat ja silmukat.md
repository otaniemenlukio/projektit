# Muuttujat ja silmukat
## Muuttujat
Muuttujat ovat keino tallentaa tietoa ohjelman sisällä. Processingissa käytetään yleensä kokonaislukumuuttujia:
```processing
void setup() {
  size(400, 400);
  stroke(255, 255, 255);
  
  int x1 = 0;
  int y2 = 50;
  int x2 = 100;
  int y2 = 200;
  
  line(x1, y1, x2, y2);
}

void draw() {
}

```

## Silmukat

Silmukoilla voi toistaa komentoja. Pythonissa on kahdenlaisia silmukoita. For-silmukat ovat hyviä listan läpikäymiseen, mutta while-silmukat ovat usein parempia. Niitä käytetään, jos toistojen määrä ei ole tiedossa etukäteen.

Silmukoiden jälkeen ohjelman suoritus jatkuu normaalisti rivi riviltä.

```processing
void setup() {
  size(400, 400);
  stroke(255, 255, 255);

  for (int i = 0; i<20; i++) {
    line(i * 20, 0, i * 20, 400);
  }
}

void draw() {
}

```
Ohjelma piirtää kaksikymmentä pystysuoraa viivaa.
Ylläolevassa esimerkissä `print(i)` ajettiin kymmenen kertaa.

While-silmukka toimii melkein kuin if. Esimerkki:

```processing
void setup() {
  size(400, 400);
  stroke(255, 255, 255);
  int i = 0;
  while (i < 20) {
    line(i * 20, 0, i * 20, 400);
    i++;

  }
}

void draw() {
}
```


While-silmukassa runkoa eli silmukan sisällä olevaa koodia ajetaan niin kauan kun ehto on tosi.
