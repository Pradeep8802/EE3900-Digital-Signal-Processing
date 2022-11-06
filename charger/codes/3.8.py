import numpy as np
from scipy import fft
from matplotlib import pyplot as plt
import os

A = 12
f = 50
scl = 400
def ddf(k):
    if(k%2==0):
        mag = 4*A/(np.pi*(1-k**2))
        plt.plot([f*k, f*k], [0, scl*np.abs(mag)],"C1",color="red")
    else:
        return 0

ddf_vec = np.vectorize(ddf)
ts = 1e-4
t = np.arange(-2/f, 2/f, ts)

# Signal
sig = A*np.abs(np.sin(2*np.pi*f*t))

sig_fft = fft.fft(sig)
sampl_freq = fft.fftfreq(sig.size, d=ts)
plt.plot(sampl_freq, np.abs(sig_fft), 'o')

ddf_vec([-8,-6,-4,-2, 0, 2, 4,6,8])
plt.grid()
plt.xlim(-10*f, 10*f)
plt.xlabel('f (Hz)')
plt.ylabel('X(f)')
plt.legend(['Simulation', 'Analysis'])
#plt.savefig('../figs/3_8.png')
plt.show()