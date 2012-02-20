#!/usr/bin/python
"""
Project Euler
Problem 3
What is the largest prime factor of the number 600851475143
Example:
>>> p3(13195)
29

"""


def primeFactors(n):
	"""
	Deterimes the prime factors of integer number n
	returns: (list) answer
	Example:
	>>> primeFactors(13195)
	[5, 7, 13, 29]
	"""
	z = n
	f = 5
	answer = []
	if z%2 == 0:
		answer.append(2)
		while z%2 == 0:
			z /= 2
	if z%3 == 0:
		answer.append(3)
		while z%3 == 0:
			z /= 3
	while f*f <= z:
		if z%f == 0:
			answer.append(f)
			while z%f == 0:
				z /= f
		if z%(f+2) == 0:
			answer.append(f+2)
			while z%(f+2) == 0:
				z /= (f+2)
		f += 6
	answer.append(z)
	return answer
	
def p3(n=600851475143):
	return max(primeFactors(n))

if __name__ == '__main__':
	import doctest
	doctest.testmod()
	p3()