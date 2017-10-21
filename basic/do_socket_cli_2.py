#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 导入socket库:
import socket

# 建立一个socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('127.0.0.1', 9999))
# 发送数据:
print(s.recv(1024).decode('utf-8'))
for data in [b'Chen', b'Cai', b'Zhang']:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
# 关闭连接:
s.send(b'exit')
s.close()
