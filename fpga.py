import numpy as np 
from scipy.stats import norm
import matplotlib.pyplot as plt
N = 100000


# P=norm.cdf(-SNR)
Y=np.zeros((N,7))

G=[[1,0,0,0,1,1,0],
   [0,1,0,0,1,0,1],
   [0,0,1,0,0,1,1],
   [0,0,0,1,1,1,1]]
H=[[1,1,0,1,1,0,0],
   [1,0,1,1,0,1,0],
   [0,1,1,1,0,0,1]]
X=np.random.binomial(1,0.5,(N,4))
Y=np.matmul(X,G)
Y=Y%2


SNR=np.linspace(1,5,10)
Pe=np.zeros((10))
for k in range(0,10):


	P=norm.cdf(-SNR[k])
	Yn=Y+np.random.binomial(1,P,(N,7))
	Yn=Yn%2

	Z=np.matmul(Yn,np.transpose(H))
	syndrome=[[0,0,0],
			  [0,0,1],
			  [0,1,0],
			  [1,0,0],
			  [1,1,1],
			  [0,1,1],
			  [1,0,1],
			  [1,1,0]]
	error=[[0,0,0,0,0,0,0],
		   [0,0,0,0,0,0,1],
		   [0,0,0,0,0,1,0],
		   [0,0,0,0,1,0,0],
		   [0,0,0,1,0,0,0],
		   [0,0,1,0,0,0,0],
		   [0,1,0,0,0,0,0],
		   [1,0,0,0,0,0,0]]
	for i in range(0,N):
		for j in range (0,7):
			if((np.equal(Z[i],syndrome[j])).all):
				Yn[i]=(Yn[i]+error[j])%2
				break

	Xd=Yn[:,[0,1,2,3]]
	Xd=np.array(Xd)
	E=(X+Xd)%2
	nE=np.zeros(N)
	for i in range(0,N):
		s=np.sum(E[i])
		if(s==0):
			nE[i]=0
		else:
			nE[i]=1
		
	n=np.sum(nE)



	Pe[k]=(n)/(N)
	n=0
	print(Pe[k])

plt.semilogy(SNR,Pe)
plt.show()