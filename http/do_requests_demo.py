import requests

r = requests.get('https://httpbin.org/')
print(type(r))
print(r.status_code)
print(type(r.text))
print(r.text)
print(r.cookies)
