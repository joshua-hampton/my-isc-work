#!/usr/bin/python

import matplotlib.pyplot as plt

fig, ax1 =  plt.subplots()

time=range(7)
co2=[250,265,272,260,300,320,389]
temp=[14.1,15.5,16.3,18.1,17.3,19.1,20.2]

ax1.plot(time,co2,'b')
ax1.set_ylabel('$CO_2$')

ax2 = ax1.twinx()

ax2.plot(time,temp,'r')
ax2.set_ylabel('Temp (deg C)')
plt.show()
plt.close()
plt.clf()

plt.subplot(1,3,1)
plt.plot(range(0,10,1))
plt.subplot(1,3,2)
plt.plot(range(10,0,-1))
plt.subplot(1,3,3)
z=[4]*10
plt.plot(z)
plt.show()
plt.clf()
