#! /usr/bin/env python
from tools import isPalindrome

def reverseProducts():
	l = [(i * j, i, j) for i in range(100,999) for j in range(100,999) if isPalindrome(str(i * j))]
	return max(l)
		
print reverseProducts()
