import numpy as np
import matplotlib.pyplot as plt
import math
import scipy
def an(a,b,n):
    if n<0:
        return 0.0
    else:
        return (a**n-b**n)/(a-b)
def bn(a,b,n):
    if n>=1:
        return an(a,b,n-1)+an(a,b,n+1)
    else:
        return 0.0
def rhs(a,b,n):
    return an(a,b,n+2)-1
a=(1+math.sqrt(5))/2
b=(1-math.sqrt(5))/2


#1.1
n=np.arange(1,100)
vec_an=scipy.vectorize(an)

def f2(a,b,n):
    return np.sum(vec_an(a,b,np.arange(n)))
vec_rhs=scipy.vectorize(rhs)
vec_f2=scipy.vectorize(f2)
l1=vec_rhs(a,b,n)
l2=vec_f2(a,b,n)
plt.subplot(211)
plt.plot(n,l1,label=r'$a_{n+2}-1$',color='r')
plt.grid()
plt.legend()
plt.subplot(212)
plt.plot(n,l2,label=r'$\sum_{k=1}^{n}a_{k}$')
plt.grid()
plt.legend()
plt.show()
#1.2
def f3(a,b,n):
   return np.dot(vec_an(a,b,np.arange(n)),np.array([1/10**i for i in range(n)]))
vec_f3=scipy.vectorize(f3)
x=np.linspace(0,100,1000)
y=np.ones(1000)*10/89
l3=vec_f3(a,b,n)
plt.plot(n,l3,label=r'$\sum_{k=1}^{n}\frac{a_{k}}{10^k}$',color='r')
plt.plot(x,y,label=r'10/89',color='b')
plt.legend()
plt.grid()
plt.show()
#1.3
def f4(a,b,n):
    return a**n+b**n
vec_bn=scipy.vectorize(bn)
vec_f4=scipy.vectorize(f4)
l4=vec_bn(a,b,n)
l5=vec_f4(a,b,n)
plt.subplot(211)
plt.plot(n,l4,label=r'$b_{n}$',color='r')
plt.grid()
plt.legend()
plt.subplot(212)
plt.plot(n,l5,label=r'$\alpha^n+\beta^n$')
plt.grid()
plt.legend()
plt.show()

#1.4
def f5(a,b,n):
   return np.dot(vec_bn(a,b,np.arange(n)),np.array([1/10**i for i in range(0,n)]))
vec_f5=scipy.vectorize(f5)
x=np.linspace(0,100,1000)
y=np.ones(1000)*8/89
l6=vec_f5(a,b,n)
plt.plot(n,l6,label=r'$\sum_{k=1}^{n}\frac{b_{k}}{10^k}$',color='r')
plt.plot(x,y,label=r'8/89')
plt.grid()
plt.legend()
plt.show()