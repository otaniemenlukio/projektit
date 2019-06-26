#include <VernierLib.h>

VernierLib Vernier;

void setup() {
  Vernier.autoID();
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
  delay(100);
}
