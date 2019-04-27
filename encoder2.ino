int x, a, b, c, d, e, f, g, y,i=0;
    
void setup() {
 pinMode(10,OUTPUT);
 pinMode(2,OUTPUT);
 pinMode(3,OUTPUT);
 pinMode(4,OUTPUT);
 pinMode(5,INPUT);
 pinMode(6,INPUT);
 pinMode(7,INPUT);
 pinMode(8,OUTPUT);

 Serial.begin(9600);
}

void loop() {
  // read x from file
  delay(10);
  i=0;
 if(Serial.available())
 {
   x=Serial.parseInt();
 
  a = (x / 8) % 2;
  b = (x / 4) % 2;
  c = (x / 2) % 2;
  d = x % 2;
  delay(100);
  digitalWrite(10,a);
  digitalWrite(2,b);
  digitalWrite(3,c);
  digitalWrite(4,d);
  digitalWrite(8,HIGH);
   delay(100);
    
  e=digitalRead(5);
  f=digitalRead(6);
  g=digitalRead(7);
//  Serial.print(e);
//  Serial.print(f);
//  Serial.print(g);
  y = a * 64 + b * 32 + c * 16 + d * 8 + e * 4 + f * 2 + g;
  delay(100);
  digitalWrite(8,LOW);
   
    Serial.println(y);
    i=i+1;
     
  
 }
 
  //write y to file
}
