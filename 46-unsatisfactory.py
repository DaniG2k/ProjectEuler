#!/usr/bin/python
from primes_sieve import primes
#####
# This problem needs a facelift.
# setting the bounds for the exponent and
# for the primes list is not efficient.
# A more efficient solution would implement a while
# loop until the smallest number is encountered.
#####
primes,exp = primes(6000),40
goldbach = set(p+2*(i**2) for p in primes for i in xrange(1,exp))
nonprimes = [n for n in xrange(1,primes[-1]) if n not in primes]

result = set()
for n in nonprimes:
    for j in xrange(1,exp):
        x = n+2*(j**2)
        if x not in goldbach and x not in primes and x%2!=0:
            result.add(x)
print min(result)
