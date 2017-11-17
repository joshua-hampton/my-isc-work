#!/usr/bin/python

import matplotlib.pyplot as plt

plt.plot(range(10))
plt.show()
plt.savefig('first_plot.png')
plt.close()

time=range(7)
co2=[250,265,272,260,300,320,389]
temp=[14.1,15.5,16.3,18.1,17.3,19.1,20.2]
plt.plot(time,co2,'b--',time,temp,'r')
plt.show()
plt.savefig('plot2.pdf')
plt.close()
