import numpy as np
from scipy.stats import randint
import matplotlib.pyplot as plt
import serial


snr =np.array([3.0,4.0,5.0,6.0,7.0])
pe=np.array([0.101,0.041,0.018,0.006,0.002])
plt.semilogy(snr,pe)
plt.grid()
plt.show()

