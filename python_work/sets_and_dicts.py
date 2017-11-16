#!/usr/bin/python

a=set([0,1,2,3,4,5])
b=set([2,4,6,8])
print a.union(b)
print a.intersection(b)


band=['mel','geri','victoria','mel','emma']
counts={}
for spice in band:
	if spice not in counts:
		counts[spice]=1
	else:
		counts[spice]+=1
for spice in counts:
	print spice, counts[spice]

if {}:
	print 'hi'

d={'maggie':'uk','ronnie':'usa'}
print 'items',d.items()
print 'keys',d.keys()
print 'values',d.values()

print d.get('russia','Nope')
short=d.setdefault('Eric','monkeyworld')
print d
