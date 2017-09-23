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

def person(name, age, **kw):
	if 'city' in kw:
		pass
	if 'job' in  kw:
		pass
	print('name:',name,'age:',age,'other:',kw)

person('zhangsan', 20, city='Chengdu')

extra = {'city':'Chengdu', 'job':'engineer'}
# person('zhangsan', 20, city=extra['city'], job=extra['job'])
person('zhangsan', 20, **extra)

person('zhangsan', 20, city='Chengdu', add='gaoxing', zipCode=610000)


