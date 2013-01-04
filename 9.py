#! /usr/bin/env python

#A Pythagorean triplet is a set of three natural numbers,
#a < b < c, for which, a2 + b2 = c2
#For example, 32 + 42 = 9 + 16 = 25 = 52.
#There exists exactly one Pythagorean triplet for which 
#a + b + c = 1000. Find the product abc.

#one simple way to find more of them is to take any 
#odd number, say 11, and square it - that's 121. 
#The two consecutive numbers that add up to 121 
#(60 and 61) give you the two other numbers (to go with 11).
#So another Pythagorean triple is 11-60-61.

for a in xrange(1, 1000):
	for b in xrange(a, 1000):
		c = 1000 - a - b
		if a*a + b*b == c*c and c > 0:
			print a,b,c
			print a*b*c
			break
