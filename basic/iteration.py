#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import Iterable

d = {'a':1, 'b':2, 'c':3}
for k,v in d.items():
    print(k,v)

for ch in 'ABC':
    print(ch)

# 判断一个str是否可迭代
print(isinstance('abc', Iterable)) # str
print(isinstance([1,2,3], Iterable)) # list
print(isinstance(123, Iterable)) # int

for i, value in enumerate(['A','B','C']):
    print(i, value)
