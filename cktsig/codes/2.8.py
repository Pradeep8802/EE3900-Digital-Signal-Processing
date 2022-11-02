import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,5e-6,100)
y=(4/3)*(1-np.exp((-3/2)*1e6*x))
ngspice=np.loadtxt('2.8.dat')


plt.plot(x,y,color="blue",label='analytical')

plt.plot(ngspice[:,0],ngspice[:,1],'o',color='orange',label='stimulation')
plt.grid()
plt.legend()
ax=plt.gca()
ax.set_xlabel('t')
ax.set_ylabel('$V_{C_0}(t)$')
plt.savefig("../figs/2.8.png")
plt.show()