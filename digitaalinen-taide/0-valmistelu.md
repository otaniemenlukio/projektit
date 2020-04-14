# Valmistelu
## Processing
Näissä työohjeissa luodaan digitaalista taidetta Processing-ohjelman avulla.
Se on helppokäyttöinen työkalu ja ohjelmointikieli, jossa keskitytään visuaalisuuteen.

### Asennus
1. Mene osoitteeseen https://processing.org/download/ ja valitse omalle laitteellesi sopiva latauslinkki. Näissä työohjeissa oletetaan, että käytät Macia, mutta suurin osa ohjeista pätee myös Windowsilla ja Linuxilla.
2. Avaa ladattu tiedosto:

3. Raahaa Processing.app Applications/Ohjelmat -kansioon

Nyt voit avata processingin samalla tavalla kuin minkä tahansa muun ohjelman.

### Ensimmäinen ohjelma
Kopioi seuraava koodinpätkä editoriin:
```processing
void setup() {
  size(400, 400);
  stroke(255, 255, 255);
  line(0, 0, 200, 200);
}
      
void draw() {

}

```

Tallenna ohjelma johonkin, josta se löytyy. Kannattaa luoda oma kansio Processing-taiteelle.

Paina vasemmassa yläkulmassa olevaa run-nappia (play-napin näköinen ympyrän sisällä) ja katso, mitä tapahtuu. Jos kaikki meni hyvin, näytölle ilmestyi ikkuna, jossa on valkoinen viiva harmaalla pohjalla.
