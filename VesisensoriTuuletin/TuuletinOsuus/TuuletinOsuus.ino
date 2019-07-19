

#include <WiFi101.h>
#include <MQTTClient.h>

#define TUULETIN A1



#define WIFI_NAME "Honor 10 Lite"
#define PASSWORD "Vikionsopo"

char wifi_name[] = WIFI_NAME;
char password[] = PASSWORD;

WiFiClient wifi_client;
MQTTClient mqtt_client;

int status = WL_IDLE_STATUS;


void setup() {
  Serial.begin(9600);

  WiFi.setPins(8, 7, 4, 2);

  while (status != WL_CONNECTED) {
    Serial.print("Yhdistetään: ");
    Serial.println(wifi_name);

    status = WiFi.begin(wifi_name, password);
    delay(10000);
  }
  Serial.println("Yhdistetty");

  mqtt_client.begin("broker.shiftr.io", wifi_client);

  while (!mqtt_client.connect("Heippahei", "aalto-shiftr-testi", "aalto-shiftr-testi")) {
    Serial.println("Yhdistetään shiftriin");
    delay(1000);
  }
  Serial.println("Yhdistetty shiftriin");

  mqtt_client.onMessage(update);
  mqtt_client.subscribe("/tuuletin");
}
void update(String &topic, String &message) {
  Serial.println(message);
  if (message.toInt()<50){
    digitalWrite(TUULETIN,0);
  }
  else{
    digitalWrite(TUULETIN,255);

  }
  


  
  
}
void loop(){

  mqtt_client.loop();
}
