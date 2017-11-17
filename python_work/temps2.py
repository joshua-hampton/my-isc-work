#!/usr/bin/python2.7

import time
import matplotlib.pyplot as plt



times=[]
temps=[]
times2=[]
temps2=[]
with open('/home/user01/my-isc-work/python_work/temps.tsv','r') as reader:
	for line in reader:
		hr_to_secs=float(line[11:13])*3600
		mins_to_secs=(float(line[14:16])*60)
		secs=float(line[17:26])
		times.append(((hr_to_secs+mins_to_secs+secs)/3600.)-1.93)
		temps.append(line[27:33])
with open('/home/user01/my-isc-work/python_work/temps2.tsv','r') as reader:
	for line in reader:
		hr_to_secs2=float(line[11:13])*3600
		mins_to_secs2=(float(line[14:16])*60)
		secs2=float(line[17:26])
		times2.append(((hr_to_secs2+mins_to_secs2+secs2)/3600.))
		temps2.append(line[27:33])

#print times2
#print times
print times[-1]-times2[-1]

plt.plot(times,temps,'r',label="Hampton's computer")
plt.plot(times2,temps2,'b',label="Whitty's computer")
plt.title('Temperature change with time')
plt.xlabel('Time since midnight (hours)')
plt.ylabel('Temperature ($^{\circ}$C)')
plt.legend()
plt.xlim([12,16])
plt.ylim([15,30])
plt.savefig('/home/user01/my-isc-work/python_work/tempgraph2.png')
plt.close()
