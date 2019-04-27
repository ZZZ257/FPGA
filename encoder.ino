int x, a, b, c, d, e, f, g, y,i=0;
  String x1;  
void setup() {
 

  Serial.begin(9600);
}

void loop() {
  // read x from file
 // delay(10);
 if(Serial.available())
 {
   x=Serial.parseInt();
  
  a = (x / 8) % 2;
  b = (x / 4) % 2;
  c = (x / 2) % 2;
  d = x % 2;
  e = a + b + d;
  e = e % 2;
  f = a + c + d;
  f = f % 2;
  g = b + c + d;
  g = g % 2;

  y = a * 64 + b * 32 + c * 16 + d * 8 + e * 4 + f * 2 + g;
  
  
    delay(100);
    Serial.println(y);
  
    delay(100);delay(100);
  
 }
  //write y to file
}
