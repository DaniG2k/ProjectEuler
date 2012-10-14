#!/usr/bin/python

def fractions(i,j):
    d = {}
    for denom in xrange(i,j):
        for num in xrange(i,j):
            num *= 1.
            if num < denom:
                d[num/denom] = num,denom
    return d

single_digit = fractions(1,10)
double_digit = fractions(10,100)

for key in single_digit:
    if key in double_digit:
        print single_digit[key],double_digit[key]
