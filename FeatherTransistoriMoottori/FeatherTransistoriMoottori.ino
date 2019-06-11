#define MOOTTORI A1
#define POTENTIOMETRI A2

void setup(){
  Serial.begin(9600);
}
void loop(){
  int potentiometri = analogRead(POTENTIOMETRI)/4;
  //Jaetaan luku neljällä, koska analogread antaa lukuja väliltä 0-1023 ja analogWrite ottaa lukuja väliltä 0-255

  Serial.println(potentiometri);
  delay(100);
  
  analogWrite(MOOTTORI, potentiometri);
}
