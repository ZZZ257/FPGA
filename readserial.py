import serial
import numpy as np
import time
ser_in = serial.Serial('/dev/ttyACM0',9600)
ser_out = serial.Serial('/dev/ttyACM0',9600)
#a = np.array([1,2,3,4,5,6,7,8,9])
#print a
#f = open()
#img=np.empty(shape=(0,0))

	#x=f.read()
time.sleep(5)
for i in range(16):
	ser_in.write(str(i))
	ser_in.write(" ")
	time.sleep(0.10)
	x = ser_out.readline()
	print (x)
	time.sleep(0.010)
# f.close()
ser_in.close
# ser_out.close
