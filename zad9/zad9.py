#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(precision=4)


def f(x):
	return 1/(1+5*x**2)
h=1/32
xw=np.linspace(-1,1,65)
fw=f(xw)
eps=np.zeros_like(xw)

size=xw.shape[0]-2
A=np.diag([4]*size,k=0)+np.diag([1]*(size-1),k=1)+np.diag([1]*(size-1),k=-1)
A=np.array(A,dtype=float)
b=np.array([fw[i-1]-2*fw[i]+fw[i+1] for i in range(1,size+1) ])
eps[1:-1]=np.linalg.solve(A,6/h**2*b)

"""
A=np.array([xw**i for i in range(0,xw.shape[0])])
wsp=np.linalg.solve(A.T,fw)
print(wsp)
def f(p):
	sum=np.zeros_like(p)
	for i in range(wsp.shape[0]):
		sum=sum+(p**i)*wsp[i]
	return sum 

"""
def l (p):
	#ktory przedzial

	num=int((p+1)/h)
	A=(xw[num+1]-p)/h
	B=(p-xw[num])/h
	C=1/6*(A**3-A)*h**2
	D=1/6*(B**3-B)*h**2
	return A*fw[num]+B*fw[num+1]+C*eps[num]+D*eps[num+1]

xp=np.arange(-1,1,0.01)
yp=np.array([l(a) for a in xp])
plt.xlim(-1.03, 1.03)
plt.ylim(-2, 2)
plt.plot(xp,yp)
plt.plot(xw,fw,'o')
plt.show()