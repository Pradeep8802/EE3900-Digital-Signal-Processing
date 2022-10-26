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
#plt.savefig('../figs/3.5png)
plt.show()



# import numpy as np
# import matplotlib.pyplot as plt
# x=np.linspace(0,5e-6,100)
# y=(2/3)*(1+np.exp(-1.5*1e6*x))

# ngspice=np.loadtxt('3.5.dat')
# plt.plot(x,y,label='Analytical',color="blue")

# plt.plot(ngspice[:,0],ngspice[:,1],'o',color='orange',label='ngspice')
# plt.xlabel('t')
# plt.ylabel(r'$V_{C_0}(t)$')
# plt.grid()
# plt.legend()
# plt.show()