#!/usr/bin/python2.7

import time
import matplotlib.pyplot as plt


while True:
	times=[]
	temps=[]
	with open('/home/user01/my-isc-work/python_work/temps.tsv','r') as reader:
		for line in reader:
			hr_to_secs=float(line[11:13])*3600
			mins_to_secs=(float(line[14:16])*60)
			secs=float(line[17:26])
			times.append((hr_to_secs+mins_to_secs+secs)/3600.)
			temps.append(line[27:33])

	#print times
	#print temps

	plt.plot(times,temps,'r')
	plt.title('Temperature change with time')
	plt.xlabel('Time since midnight (hours)')
	plt.ylabel('Temperature ($^o$C)')
	plt.savefig('/home/user01/my-isc-work/python_work/tempgraph.png')
	plt.close()
	time.sleep(10)
