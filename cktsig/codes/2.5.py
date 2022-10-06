import numpy as np
import matplotlib.pyplot as plt

x = [-4,-4,4,4,-4,-4]
y = [0,4,4,-4,-4,0]


plt.fill_between(x,y,hatch="///",facecolor='grey')
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.set_xlabel('Re(s)',loc='right')
ax.set_ylabel('Im(s)',loc='top')
x=[-4]
myticks=['-a']
plt.xticks(x,myticks)
plt.yticks()
plt.title('ROC')
plt.savefig('Circuits/figs/2.5.eps')
plt.savefig('Circuits/figs/2.5.pdf')
plt.show()