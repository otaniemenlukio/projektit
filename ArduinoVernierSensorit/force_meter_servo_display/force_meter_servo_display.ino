/* Notes about connecting the Vernier Protoboard Adapter
 * - GND to Arduino pin GND (ground)
 * - Vres to Arduino pin A4 (resistance reference)
 * - 5V to Arduino pin 5V (power)
 * - SIG1 to Arduino pin A0 (0-5V output used by almost all Vernier sensors)
 */

/* Notes about the Vernier Dual Range Force Sensor DFS-BTA:

 Vernier Factory calibration:
 
 Factory stored calibrations are:
  1 Newtons: slope = -4.9, intercept = 12.25
  scale -10 N ... 10 N
  y= kx + B
 
 */
 
/*PINS*/ 
#define PIN_SERVO 8
#define PIN_SENSOR A0

#include "Servo.h"

/* Force Scale: for Servo analogical display */
#define MIN_VAL -10
#define MAX_VAL 10

Servo myServo;
int value;
float voltage;
float force;
float previousForce;




void setup() {
  // put your setup code here, to run once:
  myServo.attach(PIN_SERVO);
  Serial.begin(115200);
  myServo.write(90);

  
  value = analogRead(PIN_SENSOR);
  voltage = value/1024.0*5.0;
  previousForce = voltage*(-4.9) + 12.25;

}

void loop() {
  // put your main code here, to run repeatedly:
  measureForce();
  updateServo();
  
  
  Serial.println(value);
  Serial.print("Force: ");
  Serial.println(force);
   
  updatePreviousForce();
  delay(10);
 
}
void measureForce(){
  value = analogRead(PIN_SENSOR);
  voltage = value/1024.0*5.0;
  force = voltage*(-4.9) + 12.25;
  }
  
void updatePreviousForce(){
  previousForce = force;
  }

void updateServo(){
  float delta = abs(force - previousForce);
  Serial.print("Servo delta: ");
  Serial.println(delta);

  if (delta > 0.5){
    int servoAngle = map(force, MIN_VAL, MAX_VAL, 180, 0);
    myServo.write(servoAngle);
    }
  }
