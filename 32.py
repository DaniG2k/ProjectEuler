#!/usr/bin/python
from tools import isPandigital
import time
start = time.time()

result = set()
for i in xrange(2,100):
    if i > 9:
        start = 123
    else:
        start = 1234
    for j in xrange(start,10001/i):
        num = int(str(i)+str(j)+str(i*j))
        # Check string for digits 1-9
        if isPandigital(num, 9):
            result.add(i*j)
print sum(result)

end = time.time()
print 'Elapsed time:',end-start
