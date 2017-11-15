#!/usr/bin/python

def double_it(number):
	return 2*number
	
def calc_hypo(a,b):
	if (type(a)==float or type(a)==int) and (type(b)==float or type(b)==int):
		hypo=((a**2)+(b**2))**0.5
	else:
		print 'Error, wrong value type'
		hypo=False
	return hypo


if __name__ == '__main__':	
	print double_it(3)
	print double_it(3.5)

	print calc_hypo(3,4)
	print calc_hypo('2',3)
