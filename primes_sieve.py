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
  if n == 1: return False
  for i in xrange(2,int(n**.5)+1):
    if n%i==0: return False
  return True
