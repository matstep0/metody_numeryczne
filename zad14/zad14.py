#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt

def g1( v ):
	x,y=v[0],v[1]
	return 2*x**2+y**2-2
def g2(v ):
	x,y=v[0],v[1]
	return (x-1/2)**2+(y-1)**2-1/4
def g( v ):
	x,y=v[0],v[1]
	w=np.array([g1(v),g2(v)])
	#print(w)
	return w
def G(v):
	a=g(v)
	return 1/2*a.T.dot(a)
def J(v):
	x,y=v[0],v[1]
	return np.array([[4*x,2*y],[2*(x-1/2),2*(y-1)]])
eps=10**-8
def znajdz(v):
	vold=np.array([1000,1000])
	while(np.linalg.norm(vold-v)>eps):
		vold=v
		z=np.linalg.solve(J(v),g(v))
		w=1

		vtest=v-w*z
		while(G(vtest)>G(v)):
			w=w/2
			vtest=v-w*z
		v=vtest
	return v


s=znajdz(np.array([1,1]))
initial=np.array([1/2,1])+ 1*np.random.rand(5,2)
for v in initial:
	a=znajdz(v)
	if(G(a)<eps):
		print("Rozwiązanie",a)
	else:
		print("Minimum lokalne",a)