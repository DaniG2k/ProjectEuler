def primes(n):
	s=range(0,n+1)
	s[1]=0
	bottom=2
	top=n//bottom
	while (bottom*bottom<=n):
		while (bottom<=top):
			if s[top]:
				s[top*bottom]=0
			top-=1
		bottom+=1
		top=n//bottom
	return [x for x in s if x]

def isPrime(n):
    n *= 1.
    basicprimes = [2,3,5,7,11]
    for b in basicprimes:
        if n%b==0 and n!=b:
            return False
        elif n==b:
            return True
    for i in xrange(12,int((n**.5+1)/6.+1)):
        if n%(6*i-1)==0 or n%(6*i+1)==0: return False
    return True

def primefactors(n):
    if n <= 3: return [n,]
    for f in xrange(2,max(3,int(n**.5))+1):
        if n%f==0: return [f,]+primefactors(n/f)
    return [n,]
