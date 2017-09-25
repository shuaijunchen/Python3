#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# _priv1是一个私有的方法，外部不能访问，把逻辑隐藏起来
def _priv1(name):
    return 'hello, %s' % name

def _priv2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _priv1(name)
    else:
        return _priv2(name)

print(greeting('world'))
