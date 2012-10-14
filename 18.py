#! /usr/bin/env python

# By starting at the top of the triangle below and moving to
# adjacent numbers on the row below, the maximum total from top to
# bottom is 23.

# Find the maximum total from top to bottom of the triangle below:
triangle = (
(75,),
(95, 64,),
(17, 47, 82,),
(18, 35, 87, 10,),
(20, 4, 82, 47, 65,),
(19, 1, 23, 75, 3, 34,),
(88, 2, 77, 73, 7, 63, 67,),
(99, 65, 4, 28, 6, 16, 70, 92,),
(41, 41, 26, 56, 83, 40, 80, 70, 33,),
(41, 48, 72, 33, 47, 32, 37, 16, 94, 29,),
(53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14,),
(70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57,),
(91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48,),
(63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31,),
(4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23),)

# For an explanation of the logic, look here:
# http://stefanoricciardi.com/2011/01/10/project-euler-problem-18-in-f/

def rowCompare(second_last, last):
	adj1, adj2 = 0, 1
	new = []
	for i in second_last:
		for j in xrange(adj1,adj2):
			new.append(max(i + last[adj1], i + last[adj2]))
		adj1 += 1
		adj2 += 1
	return new

# We essentially go through the triangle in reverse.
# We compare the last two rows, calculating the sum of adjacent nodes.

# On the next iteration, the last row becomes the sum of adjacent nodes.
# As we work our way up the triangle, we reach the greatest sum, thus
# also the maximum total from top to bottom.
def maxtotal(t):
	row = len(t) - 1
	while row > 0:
		if row == len(t) - 1:
			last = t[row]
		else:
			last = rowCompare(second_last, last)
		second_last = t[row - 1]
		#print rowCompare(second_last, last)
		if row == 1:	# We're on the second last row. Next is the solution.
			return rowCompare(second_last, last).pop()
		row -= 1

print maxtotal(triangle)
