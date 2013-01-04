#! /usr/bin/env python
from time import time
start = time()
#The following iterative sequence is defined for the set of positive integers:

#n -> n/2 (n is even)
#n -> 3n + 1 (n is odd)

#Using the rule above and starting with 13, we generate the following sequence:
#13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

#It can be seen that this sequence (starting at 13 and finishing at 1)
#contains 10 terms. Although it has not been proved yet (Collatz Problem),
#it is thought that all starting numbers finish at 1.

#Which starting number, under one million, produces the longest chain?
#NOTE: Once the chain starts the terms are allowed to go above one million.

# Recursive version
"""
def collatz(n):
	if n == 1:
		return 1
	elif n % 2 == 0:
		return 1 + collatz(n/2)
	return 1 + collatz(3*n+1)
"""

def collatz(n):
    counter = 1
    while n > 1:
        if n % 2 == 0: n /= 2
        else: n = 3*n+1
        counter += 1
    return counter

col, num = 0, 0

for n in xrange(1000000,0,-1):
    c = collatz(n)
    if c > col:
        col, num = c, n
    elif c > n:
        break

end = time()
print col,num
print 'Time:',end-start
