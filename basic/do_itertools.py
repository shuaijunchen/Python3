#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import itertools

# natuals = itertools.count(1)
# for n in natuals:
#    print(n)

cs = itertools.cycle('ABC')
for c in cs:
    print(c)
