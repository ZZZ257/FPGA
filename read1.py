import numpy as np
from scipy.stats import randint
import serial
import time
ser_in = serial.Serial('/dev/ttyACM1',9600)
ser_out = serial.Serial('/dev/ttyACM1',9600)
N=28
b=[""]
f=open("noisy.txt","rt")
g=open("output.txt","wt")
b[0]=f.read()
for i in range(N-1):
	b.append(f.read())

for i in range(N):
	
	ser_in.write(b[i])
	ser_in.write(" ")
	time.sleep(0.10)
	x = ser_out.readline()
	print (x)
	time.sleep(0.10)
	
for i in range(N):
	g.write(x)
f.close()
ser_in.close()
ser_out.close()
