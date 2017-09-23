#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Iterable
from collections import Iterator

# Iterable
print(isinstance([], Iterable)) # list
print(isinstance({}, Iterable)) # dict
print(isinstance('abc', Iterable)) # str
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable)) # int

# Iterator
print(isinstance((x for x in range(10)), Iterator))
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))

# 将生成器对象(Iterator)转换为迭代器对象(Iterator)
print(isinstance(iter([]), Iterator))
print(isinstance(iter('abc'), Iterator))
