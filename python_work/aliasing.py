#!/usr/bin/python

import copy

a=[0,1,2]
b=a
print a,b
b[0]='hello'
print a,b
a.append(3)
print a,b

c='can I change'
d=c
print c,d
d='different'
print c,d

e=[0,1,2]
f=copy.deepcopy(e)
print e,f
f[0]='hello'
print e,f
