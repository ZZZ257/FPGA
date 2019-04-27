int x, a, b, c, d, e, f, g, z,h1,h2,h3,i=0,s;
  String x1;  
void setup() {
 

  Serial.begin(9600);
}
void loop() {
  // read x from file x is code with noise
  delay(500);
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
  h1=(a+b+d+e)%2;
  h2=(a+c+d+f)%2;
  h3=(b+c+d+g)%2;
  s=h1*4+h2*2+h3;
  switch (s)
  {
 
  case 3:
  c=(c+1)%2;
  break;
  case 5:
  b=(b+1)%2;
  break;
  case 6:
  a=(a+1)%2;
  break;
  case 7:
  d=(d+1)%2;
  break;
  default:break;
  }
 // y=a*64+b*32+c*16+d*8+e*4+f*2+g;
  z=a*8+b*4+c*2+d;
    delay(100);
    Serial.println(z);
  
    
  // send z to file
 }
}
