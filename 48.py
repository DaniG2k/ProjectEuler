#! /usr/bin/python

#The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
#Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

series = [i**i for i in xrange(1,1001)]
result = str(sum(series))
print result[-10:]