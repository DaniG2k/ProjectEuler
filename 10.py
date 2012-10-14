#! /usr/bin/env python
from primes_sieve import primes

#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#Find the sum of all the primes below two million.
c = 0
for i in primes(2000000):
	c += i
print c
