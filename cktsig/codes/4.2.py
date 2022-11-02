
# Plotting VC_0(t)

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import subprocess
import shlex

def h_cont(t):
    if t < 0: 
        return 0
    else:
        return 1/3 * (1 - np.exp(-1.5e6 * t))

def h_disc(n):
    if n < 0:
        return 0
    else:
        return 1/3 * (1 - (1 - 7.5e5 * 1e-7)**(n*1e7)/(1 + 7.5e5 * 1e-7)**(n*1e7))

ht = sp.vectorize(h_cont)
hn = sp.vectorize(h_disc)
spice = np.loadtxt('4.2.dat')
T = np.linspace(0, 5e-6, 100)
plt.plot(T, ht(T), label='$h(t)$',color="green")
plt.plot(T, hn(T), '.', label='$h(n)$',color="red")
plt.plot(spice[:,0], spice[:,1], 'o', label='ngspice',color="orange")
plt.grid()
plt.legend()
plt.savefig('../figs/4.2.png')
plt.show()
