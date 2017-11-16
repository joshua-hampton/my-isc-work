#!/usr/bin/python

import numpy as np
'''
Quick code to find the maximum number of dimensions a numpy
array can have
'''

a=1
dim=[1]

while True:
	try:
		print np.zeros(dim)
		print 'number of dimensions:',len(dim)
		dim.append(a)
	except ValueError:
		print 'max number of dimensions in numpy array:',len(dim[:-1])
		exit()
