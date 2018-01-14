import socket
from urllib import request, error

try:
    response = request.urlopen('https://httpbin.org/get', timeout=0.1)
except error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('Time out')
