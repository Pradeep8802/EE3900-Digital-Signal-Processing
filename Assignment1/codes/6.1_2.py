import numpy as np
import matplotlib.pyplot as plt

N = 14
n = np.arange(N)
fn=(-1/2)**n
hn1=np.pad(fn, (0,2), 'constant', constant_values=(0))
hn2=np.pad(fn, (2,0), 'constant', constant_values=(0))
h = hn1+hn2

H = np.zeros(N) + 1j*np.zeros(N)
for k in range(0,N):
	for n in range(0,N):
		H[k]+=h[n]*np.exp(-1j*2*np.pi*n*k/N)

#print(X)
H = np.real(H)
#plots
plt.stem(range(0,N),H)
plt.title('Graph of H(k)')
plt.xlabel('$k$')
plt.ylabel('$H(k)$')
plt.grid()# minor
plt.show()
