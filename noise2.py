import numpy as np
from scipy.stats import randint
import serial
N=20
a=np.empty(7)
f = open("encoded2.txt","rt")
g=open("noisy2.txt","wt")
snr =6
var= 0.5/(10**(snr/10.0))

std=var**0.5
print(var)
c=f.readlines()
for line in c:
	x=int(line)
	#x=(int)x
	a[0]=(x/64)%2;
	a[1]=(x/32)%2;
	a[2]=(x/16)%2;
	a[3]=(x/8)%2;
	a[4]=(x/4)%2;
	a[5]=(x/2)%2;
	a[6]=x%2;
	a=a+np.random.normal(0,std,np.shape(a))
	for i in range(7):
		if (a[i]>0.5):
			a[i]=1
		else:
			a[i]=0	
	x=0
	for i in range(7):
		x=x+a[i]*(2**(6-i))
	x=int(x)	
	g.write(str(x))
	g.write("\n")
g.write("\n")	
g.close()

