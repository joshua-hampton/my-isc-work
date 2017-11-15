#!/usr/bin/python

import struct

with open('/home/user01/ncas-isc/python/exercises/example_data/weather.csv','r')  as reader:
    data=reader.read()

print data


with open('/home/user01/ncas-isc/python/exercises/example_data/weather.csv','r')  as reader:
    line=reader.readline()
    while line != '':
        print line
        line=reader.readline()
    print "This is the end..."
    
with open('/home/user01/ncas-isc/python/exercises/example_data/weather.csv','r')  as reader:
    line1=reader.readline()
    rain=[]
    for line in reader:
        r=line.strip().split(',')[-1]
        rain.append(float(r))
print rain  


with open('myrain.txt','w') as writer:
	for r in rain:
		writer.write(str(r)+'\n')


bin_data=struct.pack('bbbb',123,12,45,34)
with open('mybinary.dat','wb') as thisfile:
	thisfile.write(bin_data)
	
with open('mybinary.dat','rb') as readthisfile:
	bin_data2=readthisfile.read()
	
data=struct.unpack('bbbb',bin_data2)
print data
