#!/usr/bin/python
import re

f = open('words.txt')
re = re.compile("[A-Z]+")
for line in f:
    words = re.findall(line)
f.close()

def wordVal(w):
    sum = 0
    for char in w:
        sum += ord(char) - 64
    return sum

triangleNums = [int(.5*n*(n+1)) for n in xrange(1,20)]
result = [1 for w in words if wordVal(w) in triangleNums]

print sum(result)
