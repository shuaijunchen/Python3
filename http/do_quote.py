from urllib.parse import quote

keyword='中文'
url='http://www.baidu.com/s?wd='+quote(keyword)
print(url)
