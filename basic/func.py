#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def my_abs(x):
	if not isinstance(x, (int, float)):
		raise TypeError('bad operand type')
	if x >= 0:
		return x
	else:
		return -x

# print(my_abs('a'))

def move(x, y, step, angle=0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx, ny

# x, y = move(10, 10, 6, math.pi/0.6)
# print(x,y)
x = move(10, 10, 6, math.pi/0.6)
print(x)