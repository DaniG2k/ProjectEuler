#! /usr/bin/python
from primes_sieve import primes

primes = primes(9999)

# The next prime after 1487
primes = primes[primes.index(1493):]

for a in primes:
    b, c = a+3330, a+6660
    if b in primes and c in primes:
        a, b, c = str(a), str(b), str(c)
        if sorted(a) == sorted(b) == sorted(c):
            print '{0}{1}{2}'.format(a,b,c)
            break
