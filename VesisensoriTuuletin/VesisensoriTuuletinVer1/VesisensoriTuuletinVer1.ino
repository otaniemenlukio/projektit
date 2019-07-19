
#define MOOTTORI A1
#define VESISENSORI A2

void setup(){
  Serial.begin(9600);
}
void loop(){
  delay(100);
  int kosteus = analogRead(VESISENSORI);
  Serial.println(kosteus);//tulostetaan serialiin vesisensorin antaman luvun 0-1020

  if (kosteus < 10){ //vesisensori on tällöin kuiva
    analogWrite(MOOTTORI, 0);

  }
  else{ //vesisensori havaitsee vettä
    analogWrite(MOOTTORI, 255);

  }
  
  
}
