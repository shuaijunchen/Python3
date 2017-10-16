#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import namedtuple, deque

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)
print(p.y)

print(isinstance(p, Point))
print(isinstance(p, tuple))

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)
