#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import itertools

natuals = itertools.count(1)
# for n in natuals:
#    print(n)
ns = itertools.takewhile(lambda x:x <= 10, natuals)
print(list(ns))

# cs = itertools.cycle('ABC')
# for c in cs:
#    print(c)

# repeat() 负责把一个元素无限重复下去，不过如果提供第二个参数就可以指定重复次数
# ns = itertools.repeat('A', 3)
# for n in ns:
#    print(n)


