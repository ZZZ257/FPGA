int x, a, b, c, d, e, f, g, y,p,q,r,s;
  String x1;  
void setup() {
 pinMode(10,OUTPUT);
 pinMode(2,OUTPUT);
 pinMode(3,OUTPUT);
 pinMode(4,OUTPUT);
 pinMode(5,OUTPUT);
 pinMode(6,OUTPUT);
 pinMode(7,OUTPUT);
 pinMode(8,OUTPUT);
 pinMode(9,INPUT);
 pinMode(11,INPUT);
 pinMode(12,INPUT);
 pinMode(13,INPUT);
 
 Serial.begin(9600);
}

void loop() {
  // read x from file
  delay(10);
 if(Serial.available())
 {
   x=Serial.parseInt();
  a=(x/64)%2;
  b=(x/32)%2;
  c=(x/16)%2;
  d=(x/8)%2;
  e=(x/4)%2;
  f=(x/2)%2;
  g=x%2;
   digitalWrite(10,a);
   digitalWrite(2,b);
   digitalWrite(3,c);
   digitalWrite(4,d);
   digitalWrite(5,e);
   digitalWrite(6,f);
   digitalWrite(7,g); 
  
   digitalWrite(8,HIGH);
   
    delay(50);

    p=digitalRead(9);
    q=digitalRead(11);
    r=digitalRead(12);
    s=digitalRead(13);
    
     y = p*8+q*4+r*2+s;
    
   delay(50);
  
    digitalWrite(8,LOW);
    
    Serial.println(y);
   
     
  
 }
  //write y to file
}
