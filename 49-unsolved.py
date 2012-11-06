#! /usr/bin/python
from primes_sieve import isPrime
from itertools import permutations

perm = []

s = ''
for p in permutations('1487'):
    for n in p:
        s += n
    if isPrime(int(s)):
        perm.append(s)
    s = ''
print perm
