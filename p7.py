#!/usr/bin/python
"""
Project Euler
Problem 7
What is the 10001st prime number?
Example: 
>>> p7(6)
13
"""

from primework import euler_sieve

def p7(n=10001):
	i = 150000
	p = euler_sieve(i)
	while len(p) < n:
		i *= 2
		p = euler_sieve(i)
	return p[n-1]

if __name__ == '__main__':
	import doctest
	doctest.testmod()
	p7()