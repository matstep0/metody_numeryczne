#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(precision=4)

def f(x):
	return 1/(1+5*x**2)

xw=np.linspace(-1,1,65)
fw=f(xw)
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
	r=0
	for i in range(xw.shape[0]):
		idx=np.concatenate( (np.arange(0,i),np.arange(i+1,xw.shape[-1]))  )
		w1=np.prod(p-xw[idx])
		w2=np.prod(xw[i]-xw[idx])
		r=r+w1/w2*fw[i]
	return r

xp=np.arange(-1,1.01,0.01)
yp=np.array([l(a) for a in xp])
plt.xlim(-1.03, 1.03)
plt.ylim(-7, 1.5)
plt.plot(xp,yp)
plt.plot(xw,fw,'o')
plt.show()
