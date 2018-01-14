from urllib import request, parse

url = 'https://httpbin.org/post'
headers = {
    'Host':'httpbin.org',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

param = {
    'name':'Germey'
}

data = bytes(parse.urlencode(param), encoding='utf-8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
resp = request.urlopen(req)
print(resp.read().decode('utf-8'))
