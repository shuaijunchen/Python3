from urllib import request

req = request.Request('https://python.org')
resp = request.urlopen(req)
print(resp.read().decode('utf-8'))
