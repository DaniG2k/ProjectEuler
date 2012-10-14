#!/usr/bin/python
import time
start = time.time()

def isPandigital(n):
    x = [1,2,3,4,5,6,7,8,9]
    k = [int(i) for i in n]
    k.sort()
    return k == x

result = set()
for i in xrange(2,100):
    if i > 9:
        start = 123
    else:
        start = 1234
    for j in xrange(start,10001/i):
        check = str(i)+str(j)+str(i*j)
        if isPandigital(check):
            result.add(i*j)
print sum(result)

end = time.time()
print 'Elapsed time:',end-start
