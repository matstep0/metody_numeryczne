#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(precision=8)

A=np.diag([4]*128,k=0)+np.diag([1]*127,k=1)+np.diag([1]*127,k=-1)+np.diag([1]*124,k=4)+np.diag([1]*124,k=-4)
A=np.array(A,dtype=float)
b=np.array([1]*128,dtype=float)
Xintitial=np.array([0]*128,dtype=float) ##initial X
X=Xintitial.copy()
ilekrokow=20
#metoda G-S################################################################################3
old=[]
old.append(X.copy())
for it in range(0,ilekrokow):
    
    for i in range(128):
        s=b[i]
        if(i+1<128): s=s-A[i,i+1]*X[i+1]
        if(i+4<128): s=s-A[i,i+4]*X[i+4]
        if(i-1>=0):  s=s-A[i,i-1]*X[i-1]
        if(i-4>=0):  s=s-A[i,i-4]*X[i-4]
        X[i]=s/A[i,i]
    old.append(X.copy())

delty=np.array([np.linalg.norm(old[i+1]-old[i]) for i in range(len(old)-1)])
#print(delty)

print("wynik dla GS",np.linalg.norm( A.dot(old[-1])-b) )

#metoda gradientow################################################################################

old2=[] #zeby pierwszy krok przeszedł
def mult(p: np.array)->np.array:#szybkie mnozenie na A
    ret=np.zeros(128,dtype=float)
    for i in range(128):
        s=0
        if(i-4>=0): s=s+A[i][i-4]*p[i-4]
        if(i-1>=0): s=s+A[i][i-1]*p[i-1]
        s=s+A[i][i]*p[i]
        if(i+1<128):s=s+A[i][i+1]*p[i+1]
        if(i+4<128):s=s+A[i][i+4]*p[i+4]

        ret[i]=s
    return ret
eps=10**(-6)
X=Xintitial.copy()
old2.append(X.copy())
r=b-A.dot(X)
p=r
#while(np.linalg.norm(r)>eps):
for it in range(0,ilekrokow):
    
    rr=r.T.dot(r)
    Apk=mult(p)#A.dot(p)#trzeba pszpieszycn
    a=rr/(p.T.dot(Apk))
    r=r-a*Apk
    B=r.T.dot(r)/rr
    X=X+a*p
    p=r+B*p
    old2.append(X.copy())

delty2=np.array([np.linalg.norm(old2[i+1]-old2[i]) for i in range(len(old2)-1)])
print("wynik dla gradientow",np.linalg.norm( A.dot(old2[-1])-b))
################################################porownanie#####################

#plt.plot(delty,'o-',label='metoda Gaussa-Seidela')
#plt.plot(delty2,'o-',label='metoda gradientów sprzężonych')
#plt.ylabel('|x_n-x_n-1|')
#plt.legend()
#plt.xticks([int(i) for i in range(len(delty))])
#plt.show()
#plt.savefig('wykres.png')
