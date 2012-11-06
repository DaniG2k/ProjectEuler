#!/usr/bin/python
from primes_sieve import primes, isPrime
from time import time

start = time()
limit = 10**6
p = primes(limit)
prev_longest = 0


for i in xrange(0,len(p)):
    s, counter = 0, 0
    for num in p[i:]:
        s += num
        counter += 1
        if isPrime(s) and counter > prev_longest and s <= limit:
            prev_longest = counter
            print s, '| Terms:',counter
        elif s > limit: break

end = time()
print end-start
