# Simulaatio

Processingilla voi simuloida yksinkertaista fysiikkaa. Tässä on esimerkkinä pomppiva pallo:
```processing
void setup() {
  size(800, 800);
  background(0);
  stroke(255, 255, 255);  
}
float x = 500;
float y = 500;
float xv = 11;
float yv = 0;
float ya = 1;
float xa = 0;
void draw() {
  background(128);
  if(x>800-10/2 || x<10/2){
    xv = -xv*0.95;
  }
  if(y>800-10/2 || y<10/2){
    yv = -yv*0.95;
  }
  
  x = x + xv;
  y = y + yv;
  
  xv = xv + xa;
  yv = yv + ya;
  circle(x, y, 10);

  delay(10);
}
```
![pallo](images/pallo.png)
Kaksiuloitteinen harmoninen värähtelijä:
```processing
void setup() {
  size(800, 800);
  background(0);
  stroke(255, 255, 255);  
}
float x = 500;
float y = 500;
float xv = 11;
float yv = 0;
float k = 0.01;
void draw() {
  background(128);
  if(mousePressed){
    x = mouseX;
    y = mouseY;
    xv = mouseX-pmouseX;
    yv = mouseY-pmouseY;
  }
  x = x + xv;
  y = y + yv;
  circle(x, y, 10);
  
  xv = xv + k * (400-x);
  yv = yv + k * (400-y);
  delay(10);
}
```
