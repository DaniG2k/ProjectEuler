#! /usr/bin/python
from primes_sieve import primes, isPrime

def truncate(n, direction):
  if len(str(n)) == 1 and isPrime(n):
    return True
  elif isPrime(n):
    if direction == 'LR':
      num = int(str(n)[1:])
    elif direction == 'RL':
      num = int(str(n)[:-1])
    return truncate(num, direction)
  return False

# Generate a primes list. This is a bad
# idea and could be optimized much more.
p = primes(800000)

# The [4:] removes the unwanted values
# of 2, 3, 5 and 7.
result = [i for i in p if truncate(i, 'LR') and truncate(i, 'RL')][4:]
print result
print sum(result)
