#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from io import BytesIO

f = BytesIO()
print(f.write('中文'.encode('utf-8')))
print(f.getvalue())

b = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(b.read())

