#! /usr/bin/python
from tools import isPalindrome

print sum([i for i in xrange(1000001) if isPalindrome(str(i)) and isPalindrome(str(bin(i))[2:])])
