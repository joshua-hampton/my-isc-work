#!/usr/bin/python

s='I love to write python'
for val in s:
	print val
	
print s[4]
print s[-1]
print len(s)

print s[0], s[0][0], s[0][0][0]

split_s=s.split()
for  word in split_s:
	if word.find('i')>-1:
		print 'Code found \'i\' in',word

something='Completely different'
print dir(something)
print something.count('t')
print something.find('plete')
print something.split('e')
thing2=something.replace('different', 'silly')
print thing2
#can't do something[0] = B; strings are immutable

