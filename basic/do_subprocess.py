#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess

print('$ nslookup chenshuaijun.com')
r = subprocess.call(['nslookup', 'chenshuaijun.com'])
print('Exit code:', r)
