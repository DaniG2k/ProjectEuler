#! /usr/bin/python
from tools import divisor_sum
import time

start = time.time()

def isAbundant(n):
    if divisor_sum(n) > n:
        return True
    return False

limit = 28123
#limit = 51

abundants = [n for n in xrange(1,limit) if isAbundant(n)]

unwanted = {}
for i in abundants:
    print i
    for j in abundants:
        sum = i+j
        if sum not in unwanted:
            if sum > abundants[-1]:
                break
            elif sum in abundants:
                unwanted[sum] = [i,j]

answer = 0
for i in xrange(1,limit):
     if i not in unwanted:
         answer += i

print answer

end = time.time()
print 'Elapsed time:',end-start
