#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import types

def fn():
	pass

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

print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x : x) == types.LambdaType)
print(type(x for x in range(10)) == types.GeneratorType)