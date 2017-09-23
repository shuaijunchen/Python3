#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def power(x, n = 2):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s

print(power(5), power(5, 3))

def add_end(L=None):
	if L is None:
		L = []
	L.append('END')
	return L

print(add_end([1,2,3]))

print(add_end())

def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum+n*n
	return sum

print(calc(1,2,3))

nums = [1,2,3]
print(calc(*nums))

print(calc())
