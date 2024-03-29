#! /usr/bin/python
from math import sqrt

def isPentagonal(x):
    if sqrt(24*x+1) % 6 == 5.0 and sqrt(24*x+1) % 2 == 1.0:
        return True
    return False

pentagonals = []
i, found = 1, False
while not found:
     if isPentagonal(i):
         pentagonals.append(i)
         for p in pentagonals[:-1]:
             if isPentagonal(i + p) and isPentagonal(i - p):
                 print i-p
                 found = True
     i += 1
