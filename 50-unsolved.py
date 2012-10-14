#! /usr/bin/python
from primes_sieve import primes

p = primes(100)
pointer = 0
d = []

for i in p:
	if sum(p[:pointer]) in p:
		d.append(sum(p[:pointer]))
		print p[:pointer],sum(p[:pointer])
	pointer += 1

print d
