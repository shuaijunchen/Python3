import requests

r = requests.get('https://httpbin.org/get?name=zhangsan&age=22')
print(r.text)
