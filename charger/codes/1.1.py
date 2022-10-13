import numpy as np
import matplotlib.pyplot as plt

A=12
f_0=50
x=np.linspace(0,4/f_0,1000)
y=np.abs(A*np.sin(2*np.pi*f_0*x))
plt.plot(x,y,label=r'$|A\sin(2\pi f_0 t)|$',color='red')
plt.title('$x(t) = A|\sin(2\pi f_0t)|$')
plt.xlabel('t (in s)')
plt.legend()
plt.grid()
#plt.savefig('charger/figs/1.1.eps')
#plt.savefig('charger/figs/1.1.pdf')
plt.xlabel('t (in s)')
plt.show()




