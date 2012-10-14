#! /usr/bin/python
from fractions import gcd

def singleDigit(a,b):
    for i in a:
        for j in b:
            if i == j:
                newa = a.replace(i,'')
                newb = b.replace(j,'')
    if newa and newb:
       return int(newa),int(newb)
    return False

result_numerator = 1
result_denominator = 1

# The algorithm could be much, much better here.
for denom in xrange(10,100):
    for num in xrange(10,100):
        if num % 10 == 0 or denom % 10 == 0: pass
        elif num < denom:
            sn,sd = str(num),str(denom)
            if sn[0] in sd or sn[1] in sd:
                expected = 1.*num/denom
                if singleDigit(sn,sd):
                    sn,sd = singleDigit(sn,sd)
                    if 1.*sn/sd == expected:
                        print sn,sd,num,denom,expected
                        result_numerator *= num
                        result_denominator *= denom

print result_denominator/gcd(result_numerator,result_denominator)
