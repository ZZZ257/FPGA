import numpy as np
import serial
import time
#import matplotlib.pyplot as plt

#x = np.genfromtxt('input_fpga.csv', delimiter = ',')
#print x
#f = open("out_v1.txt",'w')
#ser = serial.Serial(
#port ='COM3', 
#baudrate = 9600, 
#parity = serial.PARITY_ODD, 
#stopbits = serial.STOPBITS_TWO, 
#bytesize = serial.EIGHTBITS
#)

ser=serial.Serial()
ser.baudrate = 9600
# ser.port ='COM3'
ser.port = 'COM3'
ser.parity = serial.PARITY_ODD
ser.stopbits = serial.STOPBITS_TWO
ser.bytesize = serial.EIGHTBITS
ser.open()
ser.write('hello')
    
# ser = serial.Serial('/dev/ttyACM2',9600)

# for i in x[0:3]:
# 	ser.write(str(i))
# 	ser.write(" ")



# 	# y = ser.readline()
# 	# f.write(y)
	

# #np.savetxt("output_100_1e5.csv", y, newline= ",", fmt = '%f')
# f.close()

# f1 = np.genfromtxt("out_v1.txt")
# print(f1.shape)
# print(f1)
# plt.plot(f1)
# plt.show()
