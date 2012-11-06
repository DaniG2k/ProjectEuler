#!/usr/bin/python
from primes_sieve import primes
from tools import isPandigital

# Tried with 987654321 but was too big.
# Went down until 7654321 and got the answer.
primes = primes(7652413)

for prime in primes[::-1]:
    if isPandigital(prime, 7):
        print prime
        break
