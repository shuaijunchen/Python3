#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import threading
import time

def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)

# 首先创建一个基于IPv4和TCP协议的socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 监听地址和端口
s.bind(('127.0.0.1', 9999))
# 开始监听
s.listen(5)
print('Waiting for connection...')
while True:
    # 接收一个新连接
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
