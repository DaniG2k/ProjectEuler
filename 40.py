#!/usr/bin/python
from time import time
start = time()

counter, digit = 0, 0
s = ''

while digit < (10**6)+1:
    counter += 1
    sc = str(counter)
    s += sc
    digit += len(sc)

print reduce(lambda x,y: x*y, [int(s[i-1]) for i in [10**j for j in range(7)]])

end = time()
print end-start
