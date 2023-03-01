#!/usr/bin/env python3
#Mateusz Stępniak Zadanie 1
import numpy as np
np.set_printoptions(precision=16)
###################################################################punkta
#tworzenie macierzy w formie jawnej
A=np.diag([4,4,4,4,4,4,4],k=0)+np.diag([1,1,1,1,1,1],k=1)+np.diag([1,1,1,1,1,1],k=-1)
A=np.array(A,dtype=float)
b=np.array([1,2,3,4,5,6,7],dtype=float)

originalA,originalb=A,b

#Algorytm
for i in range(A.shape[0]-1):
    #print("przed",A[i:i+2,i:i+3])
    xi,xj=A[i][i],A[i+1][i]
    c,s=xi/np.sqrt(xi**2+xj**2),xj/np.sqrt(xi**2+xj**2)
    obrot=np.array([[c,s],[-s,c]],dtype=float)
    b[i:i+2]=obrot.dot(b[i:i+2])
    #print(obrot)
    A[i:i+2,i:i+3]=obrot.dot(A[i:i+2,i:i+3])
    #print("po",A[i:i+2,i:i+3])
#print(A,b)
#backward susbtitution
X=np.array([0,0,0,0,0,0,0],dtype=float)
for i in range(A.shape[0]-1,-1,-1):
    #print(i)
    sum=b[i]-A[i,i+1:i+3].dot(X[i+1:i+3])
    #print(sum)
    X[i]=sum/A[i,i]

sol=np.linalg.solve(A,b)
print("Wynik za pomocą bibliotek",sol)
print("Mój wynik",X)
print("Różnica",X-sol)
print("Test poprawnosci:\n","Błąd z bibliotek:",np.linalg.norm(originalA.dot(sol)-originalb),\
    "\nBład mojego algorytmu:",np.linalg.norm(originalA.dot(X)-originalb))
print("\n\n")
##############################################################################
A,b=originalA,originalb
for i in range(A.shape[0]-1):
    #print("przed",A[i:i+2,i:i+3])
    #kasowanie dolnego
    xi,xj=A[i][i],A[6][i]
    c,s=xi/np.sqrt(xi**2+xj**2),xj/np.sqrt(xi**2+xj**2)
    xi,xj=A[i,i],A[6,i]
    A[i,i],A[6,i]=xi*c+xj*s,xi*(-s)+xj*c
    xi,xj=A[i,i+1],A[6,i+1]
    A[i,i+1],A[6,i+1]=xi*c+xj*s,xi*(-s)+xj*c
    if(i==5): c,s=1,0 #zeby nie powtarzac dwa razy
    xi,xj=A[i,5],A[6,5]
    A[i,5],A[6,5]=xi*c+xj*s,xi*(-s)+xj*c
    xi,xj=A[i,6],A[6,6]
    A[i,6],A[6,6]=xi*c+xj*s,xi*(-s)+xj*c


    xi,xj=b[i],b[6]
    b[i],b[6]=xi*c+xj*s,xi*(-s)+xj*c

    #kasowanie u gory
    xi,xj=A[i][i],A[i+1][i]
    if(i==5): xj=0 #w przedostatniej kolumnie mozemy dwa razy zrobic to samo
    c,s=xi/np.sqrt(xi**2+xj**2),xj/np.sqrt(xi**2+xj**2)
    obrot=np.array([[c,s],[-s,c]],dtype=float)
    b[i:i+2]=obrot.dot(b[i:i+2])
    #print(obrot)
    A[i:i+2,i:i+3]=obrot.dot(A[i:i+2,i:i+3])
    A[i:i+2,5:7]=obrot.dot(A[i:i+2,5:7])
    #print("po",A[i:i+2,i:i+3])
#print(A,b)
X=np.array([0,0,0,0,0,0,0],dtype=float)
for i in range(A.shape[0]-1,-1,-1):
    sum=b[i]
    if(i+2<7):sum=sum-A[i,i+2]*X[i+2]
    if(i+1<7):sum=sum-A[i,i+1]*X[i+1]
    if(i+2<6):sum=sum-A[i,6]*X[6]
    if(i+2<5):sum=sum-A[i,5]*X[5]
    X[i]=sum/A[i,i]
    #print(X[i])

sol=np.linalg.solve(A,b)
#print("sol",sol)
#print(X)
#print("ich:" ,originalA.dot(sol)-b,"\n","moje:",originalA.dot(X)-b)
print("Wynik za pomocą bibliotek",sol)
print("Mój wynik",X)
print("Różnica",X-sol)
print("Test poprawnosci:\n","Błąd z bibliotek:",np.linalg.norm(originalA.dot(sol)-originalb),\
    "\nBład mojego algorytmu:",np.linalg.norm(originalA.dot(X)-originalb))
print("\n\n")