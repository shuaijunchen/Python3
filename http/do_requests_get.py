import requests

r = requests.get('https://httpbin.org/get')
print(type(r.text))
print(r.json())
print(type(r.json()))
