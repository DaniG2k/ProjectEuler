#! /usr/bin/python

#import time
#start = time.time()

def isPandigital(num):
    if len(num) != 9 or '0' in num:
        return False
    num_list = [int(d) for d in num]
    num_list.sort()
    return num_list == [i for i in xrange(1,10)]

for multiplier in xrange(9876,9183,-1):
    concat = ''
    for n in xrange(1,3):
        concat += str(n*multiplier)
    if isPandigital(concat):
        print 'Result:',concat
        break
#end = time.time()
#print end-start
