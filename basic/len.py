#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print(len('ABC'))
print('ABC'.__len__())

class MyDog(object):
	def __len__(self):
		return 100

dog = MyDog()

print(len(dog))