//Lisätään potentiometri, jolla voidaan säädellä moottorin tehoa

#define MOOTTORI A1
#define POTENTIOMETRI A2

void setup(){
  Serial.begin(9600);
}
void loop(){
  int potentiometri = analogRead(A2)/4;
  Serial.println(potentiometri);
  delay(100);
  //Jaetaan luku neljällä, koska analogread antaa lukuja väliltä 0-1023 ja potentiometri ottaa lukuja väliltä 0-255
  
  analogWrite(MOOTTORI, potentiometri);
}
