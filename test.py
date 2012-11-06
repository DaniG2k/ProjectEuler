#!/usr/bin/python
from primes_sieve import isPrime

def prime_factorize(n):
    factors = []
    number = abs(n)
    factor = 2
    while number > 1:
        factor = get_next_prime_factor(number, factor)
        factors.append(factor)
        number /= factor
    if n < -1:
        factors[0] = -factors[0]
    return factors

def get_next_prime_factor(n, f):
    if n%2==0: return 2
    for x in range(max(f,3), int(n**.5)+1, 2):
        if n%x==0: return x
    return n
