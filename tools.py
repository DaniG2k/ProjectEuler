def fib(n):
    fib,n1,n2 = 0, 1, 0
    f = []
    while fib < n:
        n2 = fib+n1
        fib,n1 = n1,n2
        f.append(fib)
    return f

# Euclid's Algorithm
# Greatest Common Divisor
def gcd(a,b):
    if a < b: a,b = b,a # a always needs to be bigger than b
    if a%b != 0: return gcd(b, a%b)
    else: return b

# Least Common Multiple knowing the GCD
def lcm(a,b):
    return a*b/gcd(a,b)

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

def isPalindrome(n):
   return n == n[::-1]

def isPandigital(num, limit, start=1):
    num = str(num)
    x = [i for i in xrange(start,limit+1)]
    k = [int(i) for i in num]
    k.sort()
    return k == x
