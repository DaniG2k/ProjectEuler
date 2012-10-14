#! /usr/bin/env python

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.
# What is the 10001st prime number?
from primes_sieve import primes

n = 1000000
while len(primes(n)) < 10001:
	n += 1
p = primes(n)
c = 1
for i in p:
	if c <= 10001:
		print '%d) %d' % (c,i)
	c += 1
	
