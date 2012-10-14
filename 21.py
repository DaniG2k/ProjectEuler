#! /usr/bin/python
from tools import divisor_sum

result = []
for i in xrange(0,10001):
    divA = divisor_sum(i)
    divB = divisor_sum(divA)
    if divB == i and divA != divB:
        result.append(i)

print sum(result)
