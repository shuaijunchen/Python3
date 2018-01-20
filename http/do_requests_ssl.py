import requests
from requests.packages import urllib3


urllib3.disable_warnings()
response = requests.get('https://www.12306.cn/mormhweb', verify=False)
print(response.status_code)
