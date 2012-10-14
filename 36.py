#! /usr/bin/python

# Non-recursive method
def isPalindrome(n):
   return n == n[::-1]
 print sum([i for i in xrange(1000001) if isPalindrome(str(i)) and isPalindrome(str(bin(i))[2:])])


# Recursive palindrome function. A bit slower.
#def isPalindrome(n):
#	if len(n) <= 1:
#    return True
#	elif len(n) > 1:
#		if n[0] == n[-1]:
#			return isPalindrome(n[1:-1])
#		return False

#counter = [i for i in xrange(1000001) if isPalindrome(str(i)) and isPalindrome(str(bin(i))[2:])]
#print sum(counter)