#!/usr/bin/python
from itertools import permutations
import time
start = time.time()

result = []
for p in permutations('0123456789'):
    d1 = int(p[1]+p[2]+p[3])
    d2 = int(p[2]+p[3]+p[4])
    d3 = int(p[3]+p[4]+p[5])
    d4 = int(p[4]+p[5]+p[6])
    d5 = int(p[5]+p[6]+p[7])
    d6 = int(p[6]+p[7]+p[8])
    d7 = int(p[7]+p[8]+p[9])
    if d1%2==0 and d2%3==0 and d3%5==0 and d4%7==0 and d5%11==0 and d6%13==0 and d7%17==0:
        num = ''
        for i in xrange(0,10):
            num += p[i]
        result.append(int(num))
print sum(result)

end = time.time()
print 'Time elapsed:',end-start
