#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
now = datetime.now()
print(now)
print(type(now))

# 用指定日期时间创建datetime
dt = datetime(2017, 10, 16, 21, 1)
print(dt.timestamp()) # 把datetime转换为timestamp
