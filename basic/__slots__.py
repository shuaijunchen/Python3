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

def set_score(self, score):
	self.score = score

Student.set_score = set_score
s.set_score(100)
print(s.score)

class Person(object):
	__slots__ = ('name', 'age')

p = Person()
p.name = 'zhangsan'
p.age = 20
# p.score = 99
