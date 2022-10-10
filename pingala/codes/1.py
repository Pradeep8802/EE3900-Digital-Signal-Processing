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
n=np.arange(1,12)
vec_an=scipy.vectorize(an)

def f2(a,b,n):
    return np.sum(vec_an(a,b,np.arange(n)))
vec_rhs=scipy.vectorize(rhs)
vec_f2=scipy.vectorize(f2)
l1=vec_rhs(a,b,n)
l2=vec_f2(a,b,n)
#plt.subplot(211)
#plt.stem(n,l1,label=r'$a_{n+2}-1$')
#plt.grid()
#plt.legend()
#plt.subplot(212)
#plt.stem(n,l2,label=r'$\sum_{k=1}^{n}a_{k}$')
#pkadsf;kljasdfassssasdf;;l;lkjasdf;lkjadsfl;kj  adf;lk ;lkj qqwaerpawawqawerpoiuhgnghvnktyfm;thytlyhdropyhkuuuuugrgylt.grid()
#plt.legend()
#plt.savefig('../figs/1.1.png')
#plt.show()
# import numpy as np
# import matplotlib.pyplot as plt
# import math
# import scipy
# def an(a,b,n):
#     if n<0:
#         return 0.0
#     else:
#         return (a**n-b**n)/(a-b)
# def bn(a,b,n):
#     if n>=1:
#         return an(a,b,n-1)+an(a,b,n+1)
#     else:
#         return 0.0
# def rhs(a,b,n):
#     return an(a,b,n+2)-1
# a=(1+math.sqrt(5))/2
# b=(1-math.sqrt(5))/2


# #1.1
# n=np.arange(1,12)
# vec_an=scipy.vectorize(an)

def f2(a,b,n):
    return np.sum(vec_an(a,b,np.arange(n)))
vec_rhs=scipy.vectorize(rhs)
vec_f2=scipy.vectorize(f2)
l1=vec_rhs(a,b,n)
l2=vec_f2(a,b,n)
# 1.2
def f3(a,b,n):
   return np.dot(vec_an(a,b,np.arange(n)),np.array([1/10**i for i in range(n)]))
vec_f3=scipy.vectorize(f3)
x=np.linspace(0,12,12)
y=np.ones(12)*10/89
l3=vec_f3(a,b,n)
#plt.stem(n,l3,label=r'$\sum_{k=1}^{n}\frac{a_{k}}{10^k}$')
#plt.plot(x,y,label=r'10/89',color='orange')
#plt.legend()
#plt.grid()
#plt.savefig('../figs/1.2.png')
#plt.show()

#1.3
def f4(a,b,n):
    return a**n+b**n
vec_bn=scipy.vectorize(bn)
vec_f4=scipy.vectorize(f4)
l4=vec_bn(a,b,n)
l5=vec_f4(a,b,n)
# plt.subplot(211)
# plt.stem(n,l4,label=r'$b_{n}$')
# plt.grid()
# plt.legend()
# plt.subplot(212)
# plt.stem(n,l5,label=r'$\alpha^n+\beta^n$')
# plt.grid()
# plt.legend()
# #plt.savefig('../figs/1.3.png')
# plt.show()

#1.4
def f5(a,b,n):
   return np.dot(vec_bn(a,b,np.arange(n)),np.array([1/10**i for i in range(0,n)]))
vec_f5=scipy.vectorize(f5)
s=12
x=np.linspace(0,12,12)
y=np.ones(12)*8/89
l6=vec_f5(a,b,n)
plt.stem(n,l6,label=r'$\sum_{k=1}^{n}\frac{b_{k}}{10^k}$')
plt.plot(x,y,label=r'8/89',color='orange')
plt.grid()
plt.legend()
plt.savefig('../figs/1.4.png')
plt.show()
