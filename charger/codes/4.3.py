# import numpy as np
# from matplotlib import pyplot as plt
# import os

# f = 50
# V = 5
# A = 12
# N = 100000
# fc = 100
# tp = 100000
# t = np.linspace(-tp, tp, N)
# s1 = fc*np.sinc(fc*t)
# s2 = A*np.abs(np.sin(2*np.pi*f*t))
# sc = np.convolve(s1, s2, mode='same')
# plt.plot(t, sc*(np.pi*V/(2*A))*(2*tp/N))
# plt.grid()
# plt.xlabel('t (s)')
# plt.ylabel('V')
# #plt.savefig('../figs/4_3.png')
# plt.show()
#os.system('sh gopen.sh ../figs/4_3.png')
import numpy as np
import matplotlib.pyplot as plt
import scipy
def x(t):
    return 12*np.abs(np.sin(2*np.pi*50*t))
def h(t):
    return 100*np.sinc(100*t)
t=100000
vec_h=scipy.vectorize(h)
vec_x=scipy.vectorize(x)
z=np.linspace(-1e5,1e5,t)
o=np.linspace(0,2e5,t)
y=np.convolve(vec_h(z),vec_x(z))
plt.plot((5*np.pi/24)*y*2,label='simulation')
p=5*np.ones(100000)
plt.plot(o,p,color="red",label="$5$V")
plt.legend()
plt.grid()
plt.show()
