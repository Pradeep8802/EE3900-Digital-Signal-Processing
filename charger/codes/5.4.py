
import numpy as np
from matplotlib import pyplot as plt
import os
from scipy import signal


A = np.loadtxt('Chebyshev.txt')
n = 4
fc = 60
rp = 0.5
b, a = signal.cheby1(n, rp, fc, analog=True)
f, h = signal.freqs(b, a)
plt.plot(A[:,0], A[:,1], '.')
plt.semilogx(f, 20*np.log10(np.abs(h)),color="red")
plt.grid()
plt.legend(['Simulation', 'Analysis'])
#plt.savefig('../figs/5.4.png')
plt.show()