#! /usr/bin/python
from primes_sieve import isPrime

def isCircular(n):
    n = str(n)
    for k in xrange(len(n)):
        if not isPrime( int(n[k:] + n[:k]) ):
            return False
    return True

result = sum([1 for n in xrange(1,1000001) if isCircular(n)])
print result
