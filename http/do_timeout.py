from urllib import request

response = request.urlopen('https://httpbin.org/get', timeout=5)
print(response.read().decode('utf-8'))
