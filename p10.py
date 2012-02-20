#!/usr/bin/python
"""
Project Euler
Problem 10
Find the sum of all the primes below two million.
>>> p10(10)
17
"""
from primework import euler_sieve

def p10(limit=2000000):
	return sum(euler_sieve(limit))

if __name__ == '__main__':
	import doctest
	doctest.testmod()
	p10()