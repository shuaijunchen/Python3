import requests

data = {
    'name':'zhangsan',
    'age':20
}

r = requests.get('https://httpbin.org/get', params=data)
print(r.text)
