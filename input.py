import numpy as np
from scipy.stats import randint
N=20
f = open("input.txt","wt")
for i in range(N):
	b=randint.rvs(0,15)
	#b=i%16
	b=str(b)
	f.write(b)
	f.write(",")
f.close()
