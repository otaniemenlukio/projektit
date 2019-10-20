#include <Servo.h>

Servo myServo;


void setup() {
  // put your setup code here, to run once:
myServo.attach(2);
Serial.begin(115200);
myServo.write(0);
}

void loop() {
  // put your main code here, to run repeatedly:
if(Serial.available())
  {
    int value = Serial.read();
    if(value == 'o'){
      Serial.println("Lets open!" );
      myServo.write(90);
      delay(5000);
      myServo.write(0);
    }
     else if (value == 'c'){
      Serial.println("Lets Close");
      myServo.write(0);
      delay(500);
      }
    }
      

}
