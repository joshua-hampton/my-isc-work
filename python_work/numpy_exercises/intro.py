#!/usr/bin/python

import numpy as np

x=[1,2,3,4,5,6,7,8,9,10]
a1=np.array(x,dtype=np.int32)
a2=np.array(x,dtype=np.float32)
print a1.dtype, a2.dtype

a3=np.zeros((2,3,4))
print a3
a4=np.ones((2,3,4))
print a4
a5=np.arange(1000)
print a5

a=np.array([2,3.2,5.5,-6.4,-2.2,2.4])
print a[1]
print a[1:4]

b=np.array([[2, 3.2, 5.5, -6.4, -2.2,  2.4], \
            [1, 22,  4,   0.1,   5.3, -9],       \
            [3, 1,   2.1, 21,    1.1, -2]])
print'array b'
print b[:, 3]
print b[1:4,0:4]
print b[1:, 2]
