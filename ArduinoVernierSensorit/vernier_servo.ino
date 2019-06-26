#include <VernierLib.h>
#include <Servo.h>

VernierLib Vernier;
Servo servo;

#define SERVO_PIN 10

#define SENSORI_LOWER_BOUND -10
#define SENSORI_UPPER_BOUND 10

void setup() {
  Vernier.autoID();
  servo.attach(SERVO_PIN);
  Serial.begin(9600);
}
float k = 1;
float b = 0;
void loop() {
  float rawData = Vernier.readSensor();
  float sensorData = k * rawData - b;
  Serial.print(sensorData);
  Serial.print(" ");
  Serial.println(Vernier.sensorUnits());
  int angle = map(sensorData, SENSORI_LOWER_BOUND, SENSORI_UPPER_BOUND, 0, 180);
  servo.write(angle);
  Serial.println(angle);
  delay(100);
}
