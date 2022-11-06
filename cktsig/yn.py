import numpy as np
import matplotlib.pyplot as plt
import scipy
def u(n):
    if n>=0:
        return 1.00
    else:
        return 0.00
def y(n):
    a=0.5*(10**6+0.5*10**6)
    b=0.5*10**6
    if n<=0:
        return 0.00
    else:
        return (b*(u(n-1)+u(n))+(1-a)*y(n-1))/(1+a)
def f(n):
    if n>=0:
        return 2*(1-np.exp(-1.5*10**6*n))/3
x=np.linspace(0,10**-5,5)
z=np.linspace(0,10**-5,100)
vec_y=scipy.vectorize(y)
vec_f=scipy.vectorize(f)
plt.plot(x,vec_y(x),'.')
plt.plot(z,vec_f(z))
plt.grid()
plt.show()
   
