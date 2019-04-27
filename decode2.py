import numpy as np
from scipy.stats import randint
import serial
import time
ser_in = serial.Serial('/dev/ttyACM0',9600)
ser_out = serial.Serial('/dev/ttyACM0',9600)
N=20

f = open("noisy2.txt","rt")
g=open("decoded.txt","wt")
for i in range(N):
	b=f.read()	
	ser_in.write(b)
	ser_in.write("\n")
	time.sleep(0.10)
	x = ser_out.readline()
	print (x)
	g.write(x)
	time.sleep(0.10)
	
	
f.close()
g.close()
ser_in.close()
ser_out.close()
