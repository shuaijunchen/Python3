#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

L = list(range(1,11))
print(L)

# 生成[1x1, 2x2, 3x3, ..., 10x10]
L = []
for x in range(1, 11):
    L.append(x * x)
print(L)

print([x * x for x in range(1, 11) if x % 2 == 0])

print([m+n for m in 'ABC' for n in 'XYZ'])

print([d for d in os.listdir('.')])

d = {'x':'A', 'y':'B', 'z':'C'}
print([k + '=' + v for k, v in d.items()])

L = ['Hello', 'World', 18 ,'IBM', 'Apple']
print([s.lower() for s in L if isinstance(s, str)])
