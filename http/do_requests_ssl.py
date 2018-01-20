import requests

response = requests.get('https://www.12306.cn/mormhweb', verify=False)
print(response.status_code)
