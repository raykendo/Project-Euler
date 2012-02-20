#!/usr/bin/python

"""
Project Euler
Problem 2
By considering the terms in the Fibonacci sequence whose values do not 
exceed four million, find the sum of the even-valued terms.
Example:
>>> p2(100)
44
>>> p2(1000)
798
"""

def p2(limit=4000000):
	a, b = 1, 2
	answer = 0
	while b < limit:
		if b%2 == 0:
			answer += b
		a, b = b, a+b
	return answer

if __name__ == '__main__':
	import doctest
	doctest.testmod()
	p2()