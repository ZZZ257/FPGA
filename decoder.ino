void setup() {
  // put your setup code here, to run once:

}

void loop() {
  // read x from file x is code with noise
  int x,a,b,c,d,e,f,g,y,z,h1,h2,h3;
  a=(x/64)%2;
  b=(x/32)%2;
  c=(x/16)%2;
  d=(x/8)%2;
  e=(x/4)%2
  f=(x/2)%2;
  g=x%2;
  h1=a+b+d+e;
  h2=a+c+d+f;
  h3=b+c+d+g;
  s=h1*4+h2*2+h3;
  switch (s)
  case 1:
  g=(g+1)%2;
  break;
  case 2:
  f=(f+1)%2;
  break;
  case 3:
  c=(c+1)%2;
  break;
  case 4:
  e=(e+1)%2;
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
  y=a*64+b*32+c*16+d*8+e*4+f*2+g;
  z=a*8+b*4+c*2+d;
  // send z to file
  
}
