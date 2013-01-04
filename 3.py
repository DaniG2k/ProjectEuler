#! /usr/bin/env python

def isPrime(n):
	if n < 1:
		return False
	elif n == 1:
		return True
	else:
		l = [i for i in range(1, n+1) if n % i == 0]
		if l[0] == 1 and l[1] == n:
			return True
		return False

def primeFactors(num):
	l = []
	i = 2
	while i <= num:
		if isPrime(i) and num % i == 0:
			l.append(i)
			num = num / i
			#print 'num:',num
			#print 'i:',i
			#print '(num/i)',(num/i)
		else:
			i += 1
			#print 'incrementing i to',i
	return l
		

print primeFactors(600851475143)
