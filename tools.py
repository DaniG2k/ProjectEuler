def num_of_divisors(n):
    # Check the divisors up to the square root of n.
    # Then multiply by two, because n must have twofold that
    # number of divisors.
    # For a better explanation, look here:
    # http://mathschallenge.net/library/number/number_of_divisors
    return len([i for i in xrange(1,int(n**.5)) if n%i==0]) * 2

def divisor_sum(n):
    return sum(i for i in xrange(1,n) if n%i==0)

def factorial(n):
    result = 1
    for i in xrange(1,n+1):
        result *= i
    return result
