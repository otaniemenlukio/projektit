# Vesisensori tuuletin
Tehdään tuuletin joka käynnistyy, jos vesisensori havaitsee vettä. Ensimmäisessä esimerkissä moottori ja vesisensori toimivat samassa Featherissä. Vaikeammassa versiossa käytetään kahta Featheriä jotka ovat internetin kautta yhteyessä toisiinsa. 

## Versio 1
### Tarvikkeet
- Vesisensori
- Feather M0 ja siihen USB-johto
- Moottori ja siihen tuuletin
- NPN-tyyppinen transistori
- Hyppylankoja
- Kytkentäalusta

### Vesisensorin kytkentä
Vesisensorissa on kolme pinniä: plus, miinus sekä S. Pluspinni kytketään Featherin USB-portiin, miinuspinni GND-porttiin sekä S johonkin Featherin analogisista porteista. Tässä esimerkissä käytetään analogista porttia A2.

### Transistorin kytkentä
Transistorin oikeanpuoleinen pinni kytketään moottorin negatiiviseen porttiin, vasemmanpuoleinen kytketään Featherin GND-porttiin ja keskimmäinen kytketään Featherin analogiseen porttiin A1.

### Moottorin kytkentä
Moottorin positiivinen pinni kytketään käyttöjännitteeseen eli Featherin porttiin USB ja negatiivinen portti kytketään transistorin oikeanpuoleiseen pinniin.



![vesisensori](vesisensorituuletin.jpg)

