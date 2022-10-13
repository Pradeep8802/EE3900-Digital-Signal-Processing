import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

A = 12
f_0 = 50
N = 1000
t = np.linspace(0, 4/f_0, N)
B = np.ones(N) + 1j*np.zeros(N)

def acc_cos(k):
    global B
    acc = (np.exp(-1j*2*np.pi*f_0*k*t) + np.exp(1j*2*np.pi*f_0*k*t))/(1 - k**2)
    B += acc

acc_vec = sp.vectorize(acc_cos, otypes=['double'])
K = np.linspace(2, 100, 50)
acc_vec(K)
plt.plot(t, np.abs(A*np.sin(2*np.pi*f_0*t)))
plt.plot(t, 2*A*B/np.pi, '.')
plt.legend(['Analysis', 'Simulation'])
plt.grid()
plt.xlabel('t')
plt.ylabel('x(t)')
plt.show()


# import numpy as np
# from sympy import Sum,I,pi,exp,Matrix
# from sympy.abc import k
# import matplotlib.pyplot as plt

# def c(k):
#     if k%2==0:
#         return 2*A/(pi * (1- k**2))
#     else:
#         return 0

# def x(t):
    
#     a= Sum(c(k)*exp(2*I*pi*k*f_0*2),(k,-float('inf'),float('inf'))).doit()
#     return(expr1

# A = 12
# f_0 = 50

# t = np.linspace(0, 3/f_0, 100)
# plt.plot(t, np.abs(A*np.sin(2*np.pi*f_0*t)),label='$|A\sin{2\pi f_0t}|$')
# plt.plot(t,x(t),label='$\sum_{k=-\infty}^{\infty}c_ke^{j2\pi kf_0t}$')
# plt.xlabel('t')
# #plt.ylabel('x(t)')
# plt.grid()
# #plt.savefig('charger/figs/2.3.eps')
# #plt.savefig('charger/figs/2.3.pdf')
# plt.show()







#  import numpy as np
# from sympy import Sum,I,pi,exp
# from sympy.abc import k
# import matplotlib.pyplot as plt

# def c(k):
#     if k%2==0:
#         return 2*A/(np.pi * (1- k**2))
#     else:
#         return 0

# def x(t):
#     expr1 = Sum(c(k)*exp(2*I*pi*k*f_0*t),(k,-float('inf'),float('inf')))
#     return(expr1.doit())

# A = 12
# f_0 = 50

# t = np.linspace(0, 3/f_0, 250)
# plt.plot(t, np.abs(A*np.sin(2*np.pi*f_0*t)),label='$|A\sin{2\pi f_0t}|$')
# plt.plot(t,x(t),label='$\sum_{k=-\infty}^{\infty}c_ke^{j2\pi kf_0t}$')
# plt.xlabel('t')
# plt.ylabel('x(t)')
# plt.grid()
# #plt.savefig('charger/figs/2.3.eps')
# #plt.savefig('charger/figs/2.3.pdf')
# plt.show()


