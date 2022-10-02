from lcapy.discretetime import z

Xk=1/(1-z**(-1)-z**(-2))
xn=Xk.IZT()
print(Xk)
print("\n")    
Yk=(1+2*z**(-1))/(1-z**(-1)-z**(-2))
yn=Yk.IZT()
print(yn)