from urllib import request

response = request.urlopen('http://python.org')
#print(response.read().decode('utf-8'))
print(type(response))
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))
