from urllib import request
from urllib import parse

data = bytes(parse.urlencode({'word':'hello'}), encoding='utf-8')
response = request.urlopen('https://httpbin.org/post', data=data)
print(response.read().decode('utf-8'))
