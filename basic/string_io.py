#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from io import StringIO

f = StringIO()
print(f.write('hello'))
print(f.write(' '))
print(f.write('world!'))

print(f.getvalue())

s = StringIO('Hello\nHi\nGoodbye!')
while True:
	string = s.readline()
	if string == '':
		break
	print(string.strip())