#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
now = datetime.now()
print(now)
print(type(now))

# 用指定日期时间创建datetime
dt = datetime(2017, 10, 16, 21, 1)
print(dt.timestamp()) # 把datetime转换为timestamp

t = 1508158860.0
print(datetime.fromtimestamp(t)) # 本地时间
print(datetime.utcfromtimestamp(t)) # UTC时间

cday = datetime.strptime('2017-10-16 21:10:29', "%Y-%m-%d %H:%M:%S") # str转换为datetime
print(cday)

print(now.strftime('%a, %b %d %H:%M')) # datetime转换为str

# datetime加减
print(now + timedelta(hours=10))
print(now + timedelta(days=1, hours=2))
