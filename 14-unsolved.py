#! /usr/bin/env python

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

# Using recursion is slower than a while loop, but more readable.
def collatz(n):
	if n == 1:
		return 1
	elif n % 2 == 0:
		return 1 + collatz(n/2)
	else:
		return 1 + collatz(3*n+1)

# Solve using brute force
dic = {}
for i in xrange(1,1000001):
	dic[collatz(i)] = i

print dic[max(key for key, val in dic.iteritems())]
