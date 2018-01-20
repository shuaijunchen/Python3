import requests

r = requests.get('https://www.jianshu.com')
exit() if not r.status_code == requests.codes.ok else print('Request Successfully')
