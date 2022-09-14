import matplotlib.pyplot as plt
import scipy
from scipy.fft import fft,ifft
import numpy as np
N = 20
n = np.arange(N)

def x(n):
    if n < 0 or n >5 :
        return 0
    elif n < 4:
        return n + 1
    else :
        return 6-n
def y(n):
    if n < 0:
        return 0
    else :
        return x(n) + x(n-2) - y(n-1)/2
def h(n):
    return u(n)*(-1/2)**n + u(n-2)*(-1/2)**(n-2)

def u(n):
    if n < 0 :
        return 0
    else :
        return 1

def X(k,N):
    sum  = 0
    for i in range(N):
        sum += x(i)*(np.exp(-1j*2*np.pi*i*k/N))
    return sum

def H(k,N):
    sum  = 0
    for i in range(N):
        sum += h(i)*(np.exp(-1j*2*np.pi*i*k/N))
    return sum

def Y(k,N):
    return H(k,N)*X(k,N)

def y_idft(n,N):
    sum = 0
    for i in range(N):
        sum+= Y(i,N)*np.exp((2j* np.pi *i*n)/N)
    return np.real(sum)/N


vec_h = scipy.vectorize(h)
vec_x = scipy.vectorize(x)
vec_y = scipy.vectorize(y)

x_arr = vec_x(n)

h_arr = vec_h(n)

#Using IFFT 
X_k = fft(x_arr)

H_k = fft(h_arr)

Y_k = X_k*H_k

yn_Ifft= ifft(Y_k)

#Using IDFT
vec_y_idft = scipy.vectorize(y_idft)

yn_Idft = vec_y_idft(n,N)

#Using Difference Equation
yn_Diff = vec_y(n)

plt.stem(n,np.real(yn_Diff),markerfmt = 'bo')
plt.stem(n,np.real(yn_Idft),markerfmt = 'go')
plt.stem(n,np.real(yn_Ifft),markerfmt = 'ro')
plt.grid()
plt.xlabel("$n$")
plt.ylabel("$y(n)$")
plt.legend(["Difference Equation","IDFT","IFFT"])
plt.show()
