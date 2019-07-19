

#include <Adafruit_NeoPixel.h>
#include <WiFi101.h>
#include <BlynkSimpleWiFiShield101.h>


#define WIFI_SSID "Honor 10 Lite"
#define WIFI_PASS "Vikionsopo"

char auth[] ="29b8abec10b341b7a250988537b43591";


#define PIN 12    //featherissä pinni johon ledinauha on kytketty
#define NUM_LEDS 30   //ledinaudan ledejen lukumäärä


Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUM_LEDS, PIN, NEO_GRB + NEO_KHZ800);




void setup() {
   WiFi.setPins(8, 7, 4, 2);
   Blynk.begin(auth, WIFI_SSID, WIFI_PASS);

   strip.begin();
   delay(500);

   for ( uint16_t i =0; i <strip.numPixels(); i++){
     strip.setPixelColor(i, 255,255,255);
    }

   strip.setBrightness(50);
   strip.show();

}
BLYNK_WRITE(V0){ //kirkkauden säädin vidgetti kirjoittaa virtuaaliseen pinniin V0
  int brightness = param.asInt();
  strip.setBrightness(brightness);
  strip.show();
  }
BLYNK_WRITE(V1) //zeRGBa vidgetti kirjoittaa virtuaaliseen pinniin V1
{
  int red = param[0].asInt(); //values 0 or 1
  int green = param[1].asInt();
  int blue = param[2].asInt();

  for ( uint16_t i =0; i <strip.numPixels(); i++){
    strip.setPixelColor(i, red,green,blue);
    }
    strip.show();

}

void loop() {
  // put your main code here, to run repeatedly:
  Blynk.run();

}
