#!/usr/bin/python
"""
Project Euler
Problem 9
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
Example: 
>>> p9(12)
60
"""

from itertools import takewhile, count

# a + b + c = 1000
# pythagorean triple
# k(m2-n2) + k*2*m*n + k(m2+n2)
# km2 - kn2 + 2kmn + km2 + kn2
# 2km2 + 2kmn = 1000
def triple(m, n, k):
	return (k*(m*m-n*n), k*2*m*n, k*(m*m+n*n))

def p9(sumABC=1000):
	for k in takewhile(lambda x: 2*x <= sumABC, count(1)):
		for m in takewhile(lambda y: 2*(k*y*y + k*y) <= sumABC, count(1)):
			for n in takewhile (lambda z: 2*(k*m*m + k*m*z) <= sumABC, count(1)):
				if 2 * k * m * (m+n) == sumABC:
					a, b, c = k*(m*m - n*n), 2 * k * m * n, k * (m*m + n*n)
					if a > 0 and b > 0 and c > 0:
						print "k, m, n =", k, m, n
						print "a =", a
						print "b =", b
						print "c =", c
						return a*b*c
	print "Unable to calculate"
	return 0

if __name__ == '__main__':
	import doctest
	doctest.testmod()
	p9()