#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
	name = 'Student'

s = Student()
print('s.name: ', s.name)

print('Student name: ', Student.name)

s.name = 'Zhangsan'
print('s.name: ', s.name)

print('Student name: ', Student.name)

del s.name
print('del s.name: ', s.name)