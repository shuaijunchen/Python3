#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import namedtuple, deque, defaultdict, OrderedDict, Counter

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

dd = defaultdict(lambda:'N/A')
dd['key1'] = 'abc'
print(dd['key1']) # key1存在
print(dd['key2']) # key2不存在，返回默认值

# OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)
od = OrderedDict([('a', 2),('b', 2), ('c', 3)])
print(od)

od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
print(od.keys())
print(list(od.keys()))

c = Counter()
for ch in 'programming':
    c[ch] = c[ch]+1

print(c)
