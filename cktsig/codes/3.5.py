import numpy as np
import matplotlib.pyplot as plt


x=np.linspace(0,1e-6,300)
y=(2/3)*(1+np.exp((-3/2)*1e6*x))
plt.grid()
ax=plt.gca()
ax.set_xlabel('t')
ax.set_ylabel('$V_{C_0}(t)$')
simulation=np.loadtxt('3.5.dat')
ngspice=[]
for i in range(0,int(1e6),10000):
    ngspice.append(simulation[i])
ngspice=np.array(ngspice)
plt.plot(x,y,label='Analytical')
plt.scatter(ngspice[:,0],ngspice[:,1],label='Ngspice',color='orange')
plt.legend()
plt.savefig("../figs/3.5.png")
plt.show()
