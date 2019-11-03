/**
 * Ohjelma tunnistaa valoportin läpi kulkevan vesipisaran,
 * ja tulostaa csv-muodossa pudotettujen pisaroiden määrän,
 * ajan ja pudotushetken pH-arvon.
 */

int counter = 0;

void setup() {
  Serial.begin(9600);
  Serial.print("\n");
  pinMode(3,OUTPUT);
}

void loop() {
   if(analogRead(A0)<1000){
      counter+=1;
      Serial.print(counter);
      Serial.print(",");
      Serial.print(millis());
      Serial.print(",");
      Serial.print(14-(float(analogRead(A1))/1023*3.5*4));
      Serial.print("\n");
      tone(3,440);
      delay(30);
      noTone(3);
    }
}
