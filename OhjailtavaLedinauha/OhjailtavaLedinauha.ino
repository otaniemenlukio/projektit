#include <Adafruit_NeoPixel.h>

#define PIN 5
#define NUM_LEDS 30

const int trigPin = 10;
const int echoPin = 9;
long duration;
int distance;


Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUM_LEDS, PIN, NEO_GRB + NEO_KHZ800);
uint32_t magenta = strip.Color(255, 0, 255);
uint32_t tyhja = strip.Color(0, 0, 0);


void setup(){
  Serial.begin(9600);
  strip.begin();
  delay(500);
  
  pinMode (trigPin, OUTPUT);
  pinMode (echoPin, INPUT);




  

}
void loop(){
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH);

  distance = duration*0.034/2;
  Serial.println(distance);
  delay(75);

 
  strip.fill(magenta, 0, distance);
  strip.setBrightness(50);
  strip.show();

  strip.fill(tyhja, distance, 30-distance);
  strip.setBrightness(50);
  strip.show();

}
 
  
