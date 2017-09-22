#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def power(x, n = 2):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s

print(power(5), power(5, 3))
