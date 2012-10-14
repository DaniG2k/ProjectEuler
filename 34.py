#! /usr/bin/python

def factorial(n):
	f = 1
	for i in xrange(1,n+1):
		f *= i
	return f

result = 0
for i in xrange(3,99999):
	s = [factorial(int(char)) for char in str(i)]
	if sum(s) == i:
		result += i
print 'Result:',result