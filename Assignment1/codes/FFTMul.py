import numpy as np
import math

def W(n,k):
    w =  np.exp((-1j*2*math.pi*k)/n)
    return w

def I(n):
    M = np.zeros((int(n),int(n)))
    for i in range(0,int(n)):
        M[i][i] = 1
    return M

def D(n):
    M = np.zeros((int(n),int(n)),dtype=complex)
    for i in range(0,int(n)):
        M[i][i] = W(2*n,i)
    return M

def P(n):
    M = np.zeros((n,n))
    k = 0
    count = 0
    while(2*k < n):
        M[2*k][count] = 1
        k = k + 1
        count = count + 1
    k = 0
    while(count < n):
        M[2*k+1][count] = 1
        k = k + 1
        count = count + 1
    return M

def F(n):
    if(n == 1): return [[1]]

    M = np.bmat([[I(n/2),D(n/2)],[I(n/2),-D(n/2)]])
    N = np.bmat([[F(int(n/2)),np.zeros((int(n/2),int(n/2)))],[np.zeros((int(n/2),int(n/2))),F(int(n/2))]])
    A = np.matmul(M,N)
    B = np.matmul(A,P(n))
    return B

F = np.matmul(F(8),P(8))
X = [1,2,3,4,2,1,0,0]
X = np.array(X)
print(np.matmul(F,X.T))