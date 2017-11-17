#!/usr/bin/python2.7

import netCDF4

ds=netCDF4.Dataset('ggas2014121200_00-18.nc')
#for v in ds.variables:
#	print v
sst=ds.variables['SSTK']
#print sst
#for d in sst.dimensions:
#	print d, len(ds.variables[d])
#print sst.shape, sst.size
arr=sst[1,0,10:20,30:35]
#print type(arr)
dims=sst.dimensions
#print dims
vars1=ds.variables
arr_time=vars1['time'][1]
arr_level=vars1['surface'][0]
arr_lats=vars1['latitude'][10:20]
arr_lons=vars1['longitude'][30:35]
#for vals in (arr_time, arr_level,arr_lats,arr_lons):
#	print vals
metadata={}
for attr in sst.ncattrs():
	metadata[attr]=getattr(sst,attr)
#print metadata
