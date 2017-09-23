#!/usr/bin/env python3
# -*- coding: utf-8 -*-

L = [x*x for x in range(10)]
print(L)

g = (x*x for x in range(10))
print(g)

print(next(g))

for n in g:
    print(n)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

print(fib(6))
