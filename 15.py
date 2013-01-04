#! /usr/bin/env python
import time
x = time.time()

#Starting in the top left corner of a 2x2 grid, there are 6 routes 
#(without backtracking) to the bottom right corner.
#How many routes are there through a 20x20 grid?

# For combination formula, check:
#http://betterexplained.com/articles/navigate-a-grid-using-combinations-and-permutations/

def fact(n):
	if n == 0:
		return 1
	else:
		return n * fact(n - 1)

n = 20
k = 20
#print fact(n + k) / (fact(n) * fact(k))	# this version takes slightly more time
print fact(n+k) / fact(n)**2				# this takes a fraction less time
#print time.time() - x
