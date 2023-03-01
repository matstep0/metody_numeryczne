#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as P
import cmath
np.set_printoptions(4,suppress=True)
eps=10**(-8)
def L_iter(p:P,z):
	n=p.degree()
	pz=p(z)
	pd=(p.deriv(1))(z)
	pdd=(p.deriv(2))(z)
	#print((n-1)*((n-1)*pd**2-n*pz*pdd))
	m1=pd+cmath.sqrt((n-1)*((n-1)*pd**2-n*pz*pdd))
	m2=pd-cmath.sqrt((n-1)*((n-1)*pd**2-n*pz*pdd))
	m=0
	if(np.abs(m1)>np.abs(m2)): 
		m=m1 
	else:
		m=m2
	return z-(n*pz)/m

def find_z0(Pn : P,pk : P,s):
	z=s
	while(np.abs(pk(z))>eps):
		z=L_iter(pk,z)
	while(np.abs(Pn(z))>eps): #wygladzanie
		z=L_iter(Pn,z)
	return z

def  reduce(coef : list,z0):
	l=len(coef)
	b=[0]*(l-1) 
	b[-1]=coef[-1]
	#print(b,coef)
	for i in range(l-3,-1,-1):
		#print(i)
		b[i]=coef[i+1]+z0*b[i+1]
	return b
def rozwiaz(coef : list):
	W=P.Polynomial(coef)
	N=P.Polynomial(coef) #wielomian nizszego stopnia
	coefn=coef
	pier=W.degree()
	roots=[]
	for i in range(pier):
		z0=find_z0(W,N,0)
		roots.append(z0)
		coefn=reduce(coefn,z0)
		N=P.Polynomial(coefn)
		#if(np.abs(z0.imag) >eps ): # pierzemy pierwiaste sprzzony
		#	z0=z0.real-z0.imag*1j
		#	roots.append(z0)
		#	coefn=reduce(coefn,z0)
		#	N=P.Polynomial(coefn)
		#	i=i+1
	return roots

Acoef=[16,-72,-28,558,-990,783,-486,243]
Bcoef=[-4,-4,-12,-8,-11,-3,-1,2,3,1,1]
Ccoef=[1,-1j,-1,1j,1]
roots=rozwiaz(Acoef)
print(np.array(roots))
roots=rozwiaz(Bcoef)
print(np.array(roots))
roots=rozwiaz(Ccoef)
print(np.array(roots))
#A=P.Polynomial(Acoef)
#z0=find_z0(A,A,1)
#print(z0)
#print(reduce(Acoef,z0))