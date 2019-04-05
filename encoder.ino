void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
}

void loop() {
  // read x from file
  int x,a,b,c,d,e,f,g,y;
  a=(x/8)%2;
  b=(x/4)%2;
  c=(x/2)%2;
  d=x%2;
  e=a+b+d;
  e=e%2;
  f=a+c+d;
  f=f%2;
  g=b+c+d;
  g=g%2;
  
  y=a*64+b*32+c*16+d*8+e*4+f*2+g;
  //write y to file
}
