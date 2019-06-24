//Moottorin tehoa voi ohjata googlen puhetoiminnon avulla


#include <WiFi101.h>
#include <MQTTClient.h>

#define MOOTTORI A2
#define POTENTIOMETRI A1


#define WIFI_NAME "12345678"
#define PASSWORD "asdfasdf"

char wifi_name[] = WIFI_NAME;
char password[] = PASSWORD;

WiFiClient wifi_client;
MQTTClient mqtt_client;

int status = WL_IDLE_STATUS;


void setup() {
  Serial.begin(9600);

  WiFi.setPins(8, 7, 4, 2);

  while(status != WL_CONNECTED) {
    Serial.print("Yhdistetään: ");
    Serial.println(wifi_name);

    status = WiFi.begin(wifi_name, password);
    delay(10000);
  }
  Serial.println("Yhdistetty Wifiin");

  mqtt_client.begin("broker.shiftr.io", wifi_client);
  
  while (!mqtt_client.connect("asdf", "aalto-shiftr-testi", "aalto-shiftr-testi")){
    Serial.println("Yhdistetään shiftriin");
    delay(1000);
  }
  Serial.println("Yhdistetty shiftriin");
  
  mqtt_client.onMessage(update);
  mqtt_client.subscribe("/tuuletin");
}
void update(String &topic, String &message){
  Serial.println("Uusi viesti:");
  Serial.println(message);

  if(message == "full"){
    full_speed();
  }
  else if(message == "half"){
    half_speed();
  }
  else if(message == "off"){
    off();
  }
}

//Alla määritellään funktiot full_speed(), half_speed() ja off() joilla säädellään moottorin tilaa 
void full_speed(){
  analogWrite(MOOTTORI, 255);
}
void half_speed(){
  analogWrite(MOOTTORI, 160);
}
void off(){
  analogWrite(MOOTTORI, 0);
}
void loop() {
   mqtt_client.loop();
}
