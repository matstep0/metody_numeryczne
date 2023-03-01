#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(precision=4,suppress=True)


xw =np.array([0.062500, 0.187500, 0.312500, 0.437500, 0.562500, 0.687500, 0.812500, 0.937500])
fw =np.array([0.687959, 0.073443, -0.517558, -1.077264, -1.600455, -2.080815, -2.507266, -2.860307])

A=np.array([xw**i for i in range(0,xw.shape[0])])
wsp=np.linalg.solve(A.T,fw)
print(wsp)
def f(p):
	sum=np.zeros_like(p)
	for i in range(wsp.shape[0]):
		sum=sum+(p**i)*wsp[i]
	return sum 

"""
def f (p):
	r=0
	for i in range(xw.shape[0]):
		idx=np.concatenate( (np.arange(0,i),np.arange(i+1,xw.shape[-1]))  )
		w1=np.prod(p-xw[idx])
		w2=np.prod(xw[i]-xw[idx])
		r=r+w1/w2*fw[i]
	return r
"""
xp=np.arange(-1,1,0.01)
yp=np.array([f(a) for a in xp])
plt.plot(xp,yp)
plt.plot(xw,fw,'o')
plt.show()
