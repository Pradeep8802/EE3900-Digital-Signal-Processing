# Plotting VC_0(t)

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import subprocess
import shlex

def y_cont(t):
    if t < 0: 
        return 0
    else:
        return 2/3 * (1 - np.exp(-1.5e6 * t))

def y_disc(n):
    if n < 0:
        return 0
    else:
        return 2/3 * (1 - (1 - 7.5e5 * 1e-7)**(n*1e7)/(1 + 7.5e5 * 1e-7)**(n*1e7))

yt = sp.vectorize(y_cont)
yn = sp.vectorize(y_disc)
spice = np.loadtxt('4.7.dat')
T = np.linspace(0, 5e-6, 100)
plt.plot(T, yt(T), label='$y(t)$',color="green")
plt.plot(T, yn(T), '.', label='$y(n)$',color="red")
plt.plot(spice[:,0], spice[:,1], 'o', label='ngspice',color="orange")
plt.grid()
plt.legend()
plt.savefig('../figs/4.7.png')
plt.show()
