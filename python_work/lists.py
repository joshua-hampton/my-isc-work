#!/usr/bin/python

mylist=[1,2,3,4,5]

print mylist[1]
print mylist[-2]
print mylist[1:4]

one_to_ten=range(1,11)
one_to_ten[0]=10
one_to_ten.append(11)
print one_to_ten
extra=[12,13,14]
one_to_ten.extend(extra)
print one_to_ten

forward=[]
backward=[]
values=['a','b','c']
for value in values:
	forward.append(value)
	backward.insert(0,value)
print forward
print backward
print 'reverse forward: ',forward[::-1]

countries=['uk','usa','uk','uae']
print countries.count('uk')
