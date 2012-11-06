#!/usr/bin/python
# As Wikipedia explains,
# every hexagonal number is a triangular number.
# So only check pentagonal and hexagonal
def pentagonal(n): return n*(3*n-1)/2
def hexagonal(n): return n*(2*n-1)

dic = {}
for i in xrange(144,56000):
    pen = pentagonal(i)
    hex = hexagonal(i)
    if pen not in dic: dic[pen] = 1
    elif pen in dic: dic[pen] += 1
    if hex not in dic: dic[hex] = 1
    elif hex in dic: dic[hex] += 1

    if dic[pen] == 2:
        print pen
        break
