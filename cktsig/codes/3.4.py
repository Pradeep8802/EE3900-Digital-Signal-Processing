import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,1e-5,500)
y=(2/3)*(1+np.exp(-1.5*1e6*x))
z=np.ones(500)*(2/3)
plt.plot(x,y,label=r"$\frac{2}{3}(1+e^{-1.5 \times 10^6 \times t})$",color="blue")
plt.plot(x,z,label=r"$\frac{2}{3}$",color="red")
plt.xlabel('t')
plt.ylabel(r'$V_{C_0}(t)$')
plt.grid()
plt.legend()
plt.show()