import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,1e-5,300)
y=(4/3)*(1-np.exp((-3/2)*1e6*x))
z=np.ones(300)*4/3
plt.plot(x,y,label=r"$\frac{4}{3}(1-e^{-\frac{3}{2}t})u(t)$",color="blue")
plt.plot(x,z,label=r'$\frac{4}{3}$',color='red')
plt.grid()
plt.legend()
ax=plt.gca()
ax.set_xlabel('t')
ax.set_ylabel('$V_{C_0}(t)$')
plt.show()