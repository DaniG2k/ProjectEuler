#! /usr/bin/python
from time import time

start = time()
limit = 20162
abundants = []

for i in xrange(1,limit):
    c = 1
    for j in xrange(2,int(i**.5)+1):
        if i%j==0:
            c=c+j+(i/j) if j != i/j else c+j
    if c > i:
        abundants.append(i)

print sum(set(xrange(1,limit)) - set(a+b for a in abundants for b in abundants if a+b <= limit))

end = time()
print end-start
