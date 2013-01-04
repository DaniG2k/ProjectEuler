#! /usr/bin/python
from tools import divisor_sum
# 4179871

abn = []
for n in xrange(1,20162):
	d = divisor_sum(n)
	if d > n:
		abn.append(n)

#print sum(abn)
l = []
for a in abn:
	if a/2 not in abn:
		l.append(a)
print l
print sum(l)
