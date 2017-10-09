#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from types import MethodType

class Student(object):
	pass

def set_age(self, age):
	self.age = age

s = Student()
s.name = 'Student'
print(s.name)

s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)