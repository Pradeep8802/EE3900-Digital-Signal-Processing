# Reducing noise in an audio file
import soundfile as sf
from scipy import signal
import numpy as np

# Read .wav file 
input_signal, fs = sf.read('Sound_Noise.wav') 

# Sampling frequency of input signal
sampl_freq = fs
print(sampl_freq)

# Order of the filter
order = 4   
3


# Cutoff frquency is 4kHz
cutoff_freq = 4000.0  

# Digital Frequency
Wn = 2 * cutoff_freq / sampl_freq  

# b and a are numerator and denominator polynomials respectively
b, a = signal.butter(order, Wn, 'low') 
print(b)
print(a)

N = len(input_signal)
k = np.arange(N)

X = np.fft.fft(input_signal)

num = np.polyval(b, np.exp(-2j * np.pi * k / N))
den = np.polyval(a, np.exp(-2j * np.pi * k / N))
H = num / den

Y = X * H
y = np.fft.ifft(Y)

output_signal = np.real(y)
print(output_signal)

# Write the output signal into .wav file
sf.write('8_1.wav', output_signal, fs) 