"""
primework.py
Created by: Raymond K. Doman (raykendo)
Python addon for calculating prime-related functions
Used on my Project Euler solutions (http://projecteuler.net)
"""

from math import ceil
import random

def is_prime(n):
	""" 
	Determines if the number n is prime
	examples:
	>>> is_prime(2)
	True
	>>> is_prime(9)
	False
	>>> is_prime(1001)
	False
	>>> is_prime(123457)
	True
	"""
	if n == 2 or n == 3: return True
	if n < 2 or n%2 == 0: return False
	if n < 9: return True
	if n%3 == 0: return False
	r = int((n)**0.5)
	f = 5
	while f <= r:
		if n%f == 0: return False
		if n%(f+2) == 0: return False
		f +=6
	return True

def is_primelist(nlist):
	"""
	Determines which items in the list are primes.
	Examples:
	>>> is_primelist(range(10))
	[False, False, True, True, False, True, False, True, False, False]
	"""
	rlist = [True]*len(nlist)
	for n in xrange(len(nlist)):
		if nlist[n] < 2 or nlist[n]%2 == 0: rlist[n] = False
		if nlist[n]%3 == 0: rlist[n] = False
		if nlist[n] == 2 or nlist[n] == 3: rlist[n] = True
	r = int((max(nlist))**0.5)
	f = 5
	while f <= r:
		for n in xrange(len(nlist)):
			if nlist[n]%f == 0:
				if nlist[n] != f: rlist[n] = False
			if nlist[n]%(f+2) == 0:
				if nlist[n] != (f+2): rlist[n] = False
		f += 6
	return rlist

def nextprime(n):
	""" 
	Generates the next prime after number n
	>>> nextprime(123457)
	123479
	"""
	if n%2 == 0: m = n+1
	else: m = n+2
	if m==3: return m
	if m%3==0: m += 2
	while not is_prime(m):
		m += 2
		if m%3 == 0: m+= 2
	return m

def nextPrimeBig(n):
	"""
	Finds the next prime after a number
	>>> nextPrimeBig(10**12)
	1000000000039L
	"""
	if n%2 == 0: m = n+1
	else: m = n+2
	if m==3: return m
	if m%3==0: m += 2
	while not miller_rabin(m):
		m += 2
		if m%3 == 0: m+= 2
	return m

def prime_sieve(end):
	"""
	Creates a prime list. Supposed to be Sieve of Eratosthenes
	>>> primework.prime_sieve(100)
	[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
	"""
	assert end > 0, "end must be >0"
	lng = ((end // 2) - 1 + end % 2)
	sieve = [False] * (lng + 1)
	x_max, x2, xd = int(((end-1)/4.0)**0.5), 0, 4
	for xd in range(4, 8*x_max + 2, 8):
		x2 += xd
		y_max = int((end-x2)**0.5)
		n, n_diff = x2 + y_max*y_max, (y_max << 1) - 1
		if not (n & 1):
			n -= n_diff
			n_diff -= 2
		for d in range((n_diff - 1) << 1, -1, -8):
			m = n % 12
			if m == 1 or m == 5:
				m = n >> 1
				sieve[m] = not sieve[m]
			n -= d
	x_max, x2, xd = int(((end-1) / 3.0)**0.5), 0, 3
	for xd in range(3, 6 * x_max + 2, 6):
		x2 += xd
		y_max = int((end-x2)**0.5)
		n, n_diff = x2 + y_max*y_max, (y_max << 1) - 1
		if not(n & 1):
			n -= n_diff
			n_diff -= 2
		for d in range((n_diff - 1) << 1, -1, -8):
			if n % 12 == 7:
				m = n >> 1
				sieve[m] = not sieve[m]
			n -= d
	x_max, y_min, x2, xd = int((2 + (4-8*(1-end))**0.5)/4), -1, 0, 3
	for x in range(1, x_max + 1):
		x2 += xd
		xd += 6
		if x2 >= end: y_min = (((int(ceil((x2 - end)**0.5)) - 1) << 1) - 2) << 1
		n, n_diff = ((x*x + x) << 1) - 1, (((x-1) << 1) - 2) << 1
		for d in range(n_diff, y_min, -8):
			if n % 12 == 11:
				m = n >> 1
				sieve[m] = not sieve[m]
			n += d
	primes = [2, 3]
	if end <= 3:
		return primes[:max(0,end-2)]
	for n in range(5 >> 1, (int((end)**0.5)+1) >> 1):
		if sieve[n]:
			primes.append((n << 1) + 1)
			aux = (n << 1) + 1
			aux *= aux
			for k in range(aux, end, 2 * aux):
				sieve[k >> 1] = False
 
	s  = int((end)**0.5) + 1
	if s  % 2 == 0:
		s += 1
	primes.extend([i for i in range(s, end, 2) if sieve[i >> 1]]) 
	return primes

def euler_sieve(n):
	"""
	Create a candidate list within which non-primes will marked 
	as None, noting that only candidates below sqrt(n) need be checked. 
	>>> euler_sieve(100)
	[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
	"""
	candidates = range(n+1)
	fin = int(n**0.5)
	# Loop over the candidates, marking out each multiple.
	# If the current candidate is already checked off then
	# continue to the next iteration.
	for i in xrange(2, fin+1):
		if not candidates[i]: continue
		candidates[2*i::i] = [None] * (n//i - 1)
	# Filter out non-primes and return the list.
	return [i for i in candidates[2:] if i]

def prime_extend(limit, primelist):
	"""
	Extends the primelist to the new limit
	>>> prime_extend(200, prime_sieve(100))
	[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
	"""
	p = range(primelist[len(primelist)-1]+1, limit+1)
	for primes in primelist:
		if primes > (limit**0.5): break
		for pp in p:
			if not pp: continue
			if pp%primes==0: 
				p[p.index(pp)::primes] = [None] * len(p[p.index(pp)::primes])
				break
	for pp in p:
		if pp: primelist.append(pp)
	return primelist

def firstPrimeFactor(n):
	"""
	Returns the smallest prime that divides into a number
	>>> firstPrimeFactor(5183)
	71
	"""
	if n == 2 or n == 3: return n
	if n % 2 == 0: return 2
	if n < 9: return n
	if n % 3 == 0: return 3
	r = int((n)**0.5)
	f = 5
	while f <= r:
		if n%f == 0: return f
		if n%(f+2) == 0: return f+2
		f +=6
	return n

def miller_rabin_pass(a, s, d, n):
	"""
	Part of the miller_rabin function
	
	
	"""
	a_to_power = pow(a, d, n)
	if a_to_power == 1:
		return True
	for i in xrange(s-1):
		if a_to_power == n - 1:
			return True
		a_to_power = (a_to_power * a_to_power) % n
	return a_to_power == n - 1

def miller_rabin(n):
	"""
	Determines whether a large number is prime or not
	>>> miller_rabin(1000000000039)
	True
	>>> miller_rabin(1000000000037)
	False
	"""
	d = n - 1
	s = 0
	while d % 2 == 0:
		d >>= 1
		s += 1
	for repeat in xrange(20):
		a = 0
		while a == 0:
			a = random.randrange(n)
		if not miller_rabin_pass(a, s, d, n):
			return False
	return True

def miller_rabin2(n):
	"""
	Determines whether a large number is prime or not
	Does not fully work.
	>>> miller_rabin(1000000000039)
	True
	>>> miller_rabin(1000000000037)
	False
	"""
	d = n - 1
	s = 0
	while d % 2 == 0:
		d >>= 1
		s += 1
	for repeat in xrange(20):
		a = 0
		while a == 0:
			a = random.randrange(n)
		a_to_power = pow(a, d, n)
		if a_to_power != 1:
			for i in xrange(s-1):
				if a_to_power == n - 1:
					return True
				a_to_power = (a_to_power * a_to_power) % n
		if not a_to_power == n - 1:
			return False
	return True

def primeFactors(n):
	"""
	Lists the prime factors for number n
	>>> primeFactors(123456)
	[2, 3, 643]
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

if __name__ == '__main__':
	import doctest
	doctest.testmod()