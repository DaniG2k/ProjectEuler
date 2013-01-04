#! /usr/bin/env python

#Find the sum of the digits in the number 100!

def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n - 1)

i = 0
for c in str(factorial(100)):
	i += int(c)
print i
