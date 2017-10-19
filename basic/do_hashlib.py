#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

md5_ = hashlib.md5()
md5_.update('how to use md5 in '.encode('utf-8'))
md5_.update('python hashlib!'.encode('utf-8'))
print(md5_.hexdigest())

