const int trigPin = 10;
const int echoPin = 9;
const int buzzer = 3;

long duration;
int distance;

void setup() {
  pinMode (trigPin, OUTPUT);
  pinMode (echoPin, INPUT);

  pinMode (buzzer, OUTPUT);
  
  Serial.begin(9600);
}

void loop() {  
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH);

  distance = duration*0.034/2;

  
  if (distance>2){
    tone(buzzer, 500);
    delay(100);
    noTone(buzzer);
    delay(distance*10);
  }
  else{
    tone(buzzer, 500);
    delay(100);
  }
  
}
