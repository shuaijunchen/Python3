#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class a(object):
	pass

print(type(123))
print(type('abc'))
print(type(None))
print(type(abs))
print(type(a()))


# Type comparison
print(type(123)== type(456))
print(type(123)== int)
print(type('str')== type('abc'))
print(type('123')== str)
print(type('123')== type(123))