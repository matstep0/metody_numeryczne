#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
#trzeba policzyc 0-17
ba=17
stos=[]
def f(t): 
	return np.cos((1+t)/(0.04+t**2))*np.exp(-t**2)

def I(c,d):
	return (d-c)/2*(f(c)+f(d))

def F(a,b):
	tol=10**(-8)
	a=a
	b=b
	sum=0
	stack=[(a,b)]
	while(len(stack)>0):
		last=stack[-1]
		stack.pop()
		(c,e)=last
		d=(c+e)/2
		w=I(c,e)
		if(e-c<10**-8) : break
		w1=I(c,d)
		w2=I(d,e)
		err=np.abs(1/3*(w1+w2-w))
		#print(err)
		#print("glupie",(e-c)*tol/(b-a))
		#print(e-c,tol,b-a)
		if err<(e-c)*tol/(b-a):
			sum=sum+4/3*(w1+w2)-1/3*w
		else:
			stack.append((d,e))
			stack.append((c,d))
	return sum

print(F(-19,19))

step=0.001
xp=np.arange(-20,20,step)
yp=np.array([ F(x,x+step) for x in xp])
yp=np.cumsum(yp)
#plt.xlim(-1.03, 1.03)
#plt.ylim(-7, 1.5)
plt.plot(xp,yp)
#plt.plot(xw,fw,'o')
plt.title("F(x)")
plt.show()
"""

while(err>tolerance):
	iter=iter+1
	h=h/2
	suma=lepszypodzial(suma,h)
	nowy=np.zeros(iter+1)
	nowy[0]=Ak=h*suma
	for i in range(1,nowy.shape[0]):
		nowy[i]=(4**iter*nowy[i-1]-A[-1][i-1])/(4**iter-1)
	err=np.abs(nowy[-1]-A[-1][-1])
	A=nowy.copy()
	print(Ak,nowy[-1],err)

#for i in range(10):
#	h=h/2
#	suma=lepszypodzial(suma,h)
#	print(suma*h)
"""