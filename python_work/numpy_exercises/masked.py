#!/usr/bin/python

import numpy as np
import numpy.ma as MA


marr=MA.masked_array(range(10),fill_value=-999)
print marr
print marr.fill_value
marr[2]=MA.masked
print marr
print marr.mask

narr=MA.masked_where(marr>6,marr)
print narr

print narr.fill_value
print MA.filled(narr)
print type(MA.filled(narr))

m1=MA.masked_array(range(1,9))
print 'm1',m1
m2=m1.reshape(2,4)
print 'm2',m2

m3=MA.masked_where(m2>6,m2)
print 'm3',m3

print m3*100

m4=m3-np.ones([2,4])
print 'm4',m4
print type(m4)
