import numpy as np
import scipy as sc
import matplotlib.pyplot as plt

def xn(n):
    if n<0:
        return 0
    #if 0<=n<=1:
    elif n==0:
        return 1
    elif n==1:
        return 1
    else:
        return xn(n-1)+xn(n-2)

def yn(n):
	return xn(n-1)+xn(n+1)
n=np.arange(10)
vec_xn=sc.vectorize(xn)
vec_yn=sc.vectorize(yn)

#2.2
plt.stem(n,vec_xn(n))
plt.xlabel("n")
plt.ylabel("x(n)")
plt.grid()
plt.show()


#2.5
plt.stem(n,vec_yn(n))
plt.xlabel("n")
plt.ylabel("y(n)")
plt.grid()
plt.show()