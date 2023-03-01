#!/usr/bin/python3
import numpy as np
#trzeba policzyc 0-17
ba=17
def f(x): return np.sin(np.pi*(1+np.sqrt(x))/(1+x**2))*np.exp(-x)

def lepszypodzial(suma,h):
	it=h
	while(it<ba):
		suma=suma+f(it)
		it=it+2*h
	return suma

suma=f(0)/2+f(17)/2
h=ba
A=[np.array([suma*h])]
iter=0
err=10000
tolerance=10**(-7)

while(err>tolerance):
	iter=iter+1
	h=h/2
	suma=lepszypodzial(suma,h)
	nowy=np.zeros(iter+1)
	nowy[0]=Ak=h*suma
	for i in range(1,nowy.shape[0]):
		nowy[i]=(4**iter*nowy[i-1]-A[-1][i-1])/(4**iter-1)
	err=np.abs(nowy[-1]-A[-1][-1])
	A.append(nowy.copy())
	print(Ak,nowy[-1],err)

#for i in range(10):
#	h=h/2
#	suma=lepszypodzial(suma,h)
#	print(suma*h)