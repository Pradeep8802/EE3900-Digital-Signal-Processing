import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize as op

fft_times = np.loadtxt('fft_times.dat', dtype=float)
conv_times = np.loadtxt('conv_times.dat', dtype=float)

N = np.logspace(1, len(fft_times), num=len(fft_times), base=2)

fft_fit = op.curve_fit(lambda x,a : a*x*np.log(x), N, fft_times)[0]
conv_fit = op.curve_fit(lambda x,a : a*x*x, N, conv_times)[0]

plt.plot(N, fft_fit * N * np.log(N), label='$O(n \log n)$')
plt.plot(N, conv_fit * N * N, label='$O(n^2)$')
plt.plot(N, fft_times, 'x', label='FFT-IFFT')
plt.plot(N, conv_times, 'x', label='Convolution')
plt.xlabel('Input size')
plt.ylabel('Running time')
plt.title('Comparison between running times of FFT-IFFT and Convolution')
plt.legend()
plt.grid()
plt.show()