#! /usr/bin/python

grid = 1001**2
spiral = [1]
gap = 2
append_count = 0

for i in xrange(grid + 1):
	for j in xrange(0,3):
		if append_count == 4:
			# The number gap increases by 2, 4, then 6 and so on
			gap += 2
			append_count = 0

		if i == spiral[-1] + gap:
			spiral.append(i)
			append_count += 1

print sum(spiral)