#!/usr/bin/python
from primes_sieve import primefactors

numfactors = 4
# The first number to have 4 prime factors
c = 2*3*5*7
while True:
    if len(set(primefactors(c))) == numfactors:
        if len(set(primefactors(c+1))) == numfactors:
            if len(set(primefactors(c+2))) == numfactors:
                if len(set(primefactors(c+3))) == numfactors:
                    print 'Result:',c
                    break
            else: c+=1
        else: c+=1
    c += 1
