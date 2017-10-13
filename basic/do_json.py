#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
d = dict(name='Chen', age=20, score=100)
print(json.dumps(d))

json_str = '{"score": 100, "age": 20, "name": "Chen"}'
print(json.loads(json_str))
