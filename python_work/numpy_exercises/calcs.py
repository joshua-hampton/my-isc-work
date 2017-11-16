#!/usr/bin/python

import numpy as np

def magcalc(u,v):
	mag=((u**2)+(v**2))**0.5
	magarr=np.where(mag<0.1,0.1,mag)
	return magarr


a=np.array([range(4),range(10,14)])
print a
b=np.array([2,-1,1,0])
print b
print ' '
print a*b

b1=b*100
b2=b*100.0

print b1
print b2

print b1==b2

print b1.dtype, b2.dtype

arr=np.arange(10)
print arr < 3
print np.less(arr,3)

condition=np.logical_or(arr<3,arr>8)
print np.where(condition,arr*5,arr*-5)

u=np.array([[4,5,6],[2,3,4]])
v=np.array([[2,2,2],[1,1,1]])
print magcalc(u,v)

u1=np.array([[4,5,0.01],[2,3,4]])
v1=np.array([[2,2,0.03],[1,1,1]])
print magcalc(u1,v1)

