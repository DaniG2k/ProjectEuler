#! /usr/bin/env python

fib = 0
n1 = 0
n2 = 1
c = 0
for i in xrange(1,1000000):
	fib = n1 + n2
	n1 = n2
	n2 = fib
	c += 1
	if len(str(n1)) == 1000:
		print n1
		print c
		break
