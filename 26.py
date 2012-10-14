#! /usr/bin/python
import re

# We could check only prime numbers since those are
# the ones that yield the longest recurring cycles.
# This would speed up the code quite a bit.
#
# from primes_sieve import primes
# p = primes(1000)

# Using regexp to find a pattern.
# However, this method forces me to selected an arbitrary
# exponent (10**n/i). It doesn't work with smaller exponents
# but seems to do the trick on large ones as the decimal
# becomes more precise.
d = 0
longest = 0
pattern = re.compile(r"([0-9]+?)\1+")

for i in xrange(3,1001):
    if i % 2 == 0 or i % 5 == 0: pass
    patterns = pattern.findall(str(10**2000/i))
    for num in patterns:
        if len(str(num)) >= len(str(longest)):
            longest = num
            d = i
print d
