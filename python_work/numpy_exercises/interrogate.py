#!/usr/bin/python

import numpy as np

arr=np.array([range(4),range(10,14)])
print np.shape(arr)
print np.size(arr)
print np.max(arr)
print np.min(arr)

print np.reshape(arr,(2,2,2))
print np.transpose(arr)
print np.ravel(arr)
print arr.astype(np.float64)
