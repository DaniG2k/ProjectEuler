#! /usr/bin/env python

def triangle(n):
	return sum([i for i in xrange(n+1)])

def factors(n):
	return [i for i in xrange(1,n+1) if n % i == 0]
