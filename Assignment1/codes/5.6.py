def u(n):
    if n <0 :
        return 0.0
    else :
        return 1.0
def h(n):
    return u(n)*(-1.0/2)**n + u(n-2)*(-1.0/2)**(n-2)
summation = 0    
for i in range(10000):
    summation +=h(i)
print(summation)    
