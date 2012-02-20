#!/usr/bin/python
"""
Project Euler
Problem 1
Find the sum of all the multiples of 3 or 5 below 1000.
Example: 

>>> p1(3, 5, 10)
23
"""
def p1(a=3, b=5, limit=1000):
	return sum([i for i in xrange(a, limit, a)]) + sum([i for i in xrange(b, limit, b)]) - sum([i for i in xrange(a*b, limit, a*b)])

if __name__ == '__main__':
	import doctest
	doctest.testmod()
	p1()