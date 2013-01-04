#!/usr/bin/python

def sameDigits(n1,n2):
    return sorted(str(n1)) == sorted(str(n2))

# Recurisve check
def rCheck(mult, i):
    if mult == 5 and sameDigits(mult*i, 6*i):
        print i
        return True
    elif sameDigits(mult*i, (mult+1)*i):
        return rCheck(mult+1, i)
    return False

i = 1
while not rCheck(2, i):
    i += 1

"""
#Non-recursive alternative:

i, mult = 1, 2

while True:
    if sameDigits(mult*i, (mult+1)*i) and sameDigits((mult+1)*i, (mult+2)*i) and sameDigits((mult+2)*i, (mult+3)*i) and sameDigits((mult+3)*i, (mult+4)*i):
        print i
        break
    i += 1
"""
