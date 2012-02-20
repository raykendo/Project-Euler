#!/usr/bin/python
"""
Project Euler
Problem 5
What is the smallest positive number that is evenly divisible 
by all of the numbers from 1 to 20?
Example: 

>>> p5(10)
2520
"""

def p5(maxN):
	divisors = {}
	for i in xrange(2, maxN + 1):
		j = i
		f = 2
		while j > 1:
			while j%f != 0:
				f += 1
			count = 0
			while j%f == 0:
				count += 1
				j /= f
			if f in divisors:
				if divisors[f] < count:
					divisors[f] = count
			else:
				divisors[f] = count
			f += 1
	answer = 1
	for i in divisors:
		answer *= i**divisors[i]
	return answer

if __name__ == '__main__':
	import doctest
	doctest.testmod()
	p5()