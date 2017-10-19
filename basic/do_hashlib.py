#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib

s = 'how to use md5 in python hashlib?'

md5 = hashlib.md5()
md5.update(s.encode('utf-8'))
print(md5.hexdigest())

md5_ = hashlib.md5()
md5_.update('how to use md5 in '.encode('utf-8'))
md5_.update('python hashlib!'.encode('utf-8'))
print(md5_.hexdigest())

sha1 = hashlib.sha1()
sha1.update(s.encode('utf-8'))
print(sha1.hexdigest())

