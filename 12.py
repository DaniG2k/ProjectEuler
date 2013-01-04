from tools import num_of_divisors
import time

start = time.time()

def triangle(n):
	return (n*(n+1))/2

counter = 1
found = False

while found == False:
    n = triangle(counter)
    # The triangle number presumably has these
    # basic (prime) divisors, since it needs to have
    # at least 500.
    if n%2==0 and n%3==0 and n%5==0 and n%7==0 and n%11==0:
        divs = num_of_divisors(n)
        if divs >= 500:
            print n,'has',divs,'divisors.'
            end = time.time()
            found = True
    counter += 1

print 'Time elapsed:',end-start
