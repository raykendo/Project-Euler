#!/usr/bin/python
"""
Project Euler
Problem 4
Find the largest palindrome made from the product of two 3-digit numbers.
Example:
>>> p4(2)
9009
"""

def p4(n=3):
	"""
	param: n (int) number of digits to calculate through
	returns: maxX (int) maximum palindrome
	"""
	maxX = 0
	for a in xrange(10**(n-1), 10**n):
		for b in xrange(10**(n-1), a+1):
			c = a*b
			strc = str(c)
			if strc == ''.join(reversed(strc)):
				if c > maxX:
					maxX = c
	return maxX

if __name__ == '__main__':
	import doctest
	doctest.testmod()
	p4()