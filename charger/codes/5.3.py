import numpy as np
from matplotlib import pyplot as plt
import os
from scipy import signal

A = np.loadtxt('butter.txt')
n = 5
fc = 60
b, a = signal.butter(n, fc, analog=True)
f, h = signal.freqs(b, a)
plt.plot(A[:,0], A[:,1], '.')
plt.semilogx(f, 20*np.log10(np.abs(h)),color="red")
plt.grid()
plt.legend(['Simulation', 'Analysis'])
#plt.savefig('../figs/5.3.png')
plt.show()