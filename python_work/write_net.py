#!/usr/bin/python

import datetime
from netCDF4 import Dataset
from csv import reader
import numpy as np

#Ex8
def convert_time(tm):
	tm=datetime.datetime.strptime(tm,'%Y-%m-%d %H:%M:%S.%f')
	return tm
#Ex9
def convert_temp(tc):
	tk=float(tc.strip('+').strip('C'))+273.15
	return tk
#Ex10	
infile = '/home/user01/my-isc-work/python_work/temps_save.tsv'
outfile = '/home/user01/my-isc-work/python_work/temps_save.nc'

times=[]
temps=[]

with open(infile,'rb') as tsvfile:
	tsvreader=reader(tsvfile,delimiter='\t')
	for row in tsvreader:
		times.append(convert_time(row[0]))
		temps.append(convert_temp(row[1]))
#Ex11
dataset = Dataset(outfile, "w", format='NETCDF4_CLASSIC')

initial_time = times[0]
time_values = []

for t in times:
    value = t - initial_time
    ts = value.total_seconds()
    time_values.append(ts)


time_units = "seconds since " + initial_time.strftime('%Y-%m-%d %H:%M:%S')

time_dim=dataset.createDimension("time", None)

time_var=dataset.createVariable("time", np.float64, ("time",))
time_var[:] = time_values
time_var.units = time_units
time_var.standard_name = "time"
time_var.calendar = "standard"

temp_var=dataset.createVariable('temp',np.float64,('time',))
temp_var[:]=temps
temp_var.units='K'
temp_var.standard_name='air_temperature'

dataset.Conventions  =  "CF-1.6" 
dataset.institution  =  "Hampton, NCAS"   
dataset.title  =  "My   first CF-netCDF   file" 
dataset.history   =  "%s:  Written  with  script:  write_sensor_data_to_netcdf.py"  %  (datetime.datetime.now().strftime("%x  %X"))

dataset.close()


