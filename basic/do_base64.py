#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base64

print(base64.b64encode(b'python!'))
print(base64.b64decode(b'cHl0aG9uIQ=='))

print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64decode(b'abcd--__'))

