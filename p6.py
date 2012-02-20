#!/usr/bin/python
"""
Project Euler
Problem 6
Find the difference between the sum of the squares of the first 
one hundred natural numbers and the square of the sum.
Example: 
>>> p6(10)
2640
"""

def p6(limit=100):
	return (sum(i for i in xrange(limit + 1)))**2 - sum(i * i for i in xrange(limit + 1))

if __name__ == '__main__':
	import doctest
	doctest.testmod()
	p6()