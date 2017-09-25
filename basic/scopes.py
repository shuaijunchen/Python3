#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
