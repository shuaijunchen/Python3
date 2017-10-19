#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request

req = request.Request('https://api.douban.com/v2/book/2129650')
req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36')
with request.urlopen(req) as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s:%s' % (k, v))
    print('Data:', data.decode('utf-8'))
