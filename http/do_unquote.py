from urllib.parse import unquote

url = 'http://www.baidu.com/s?wd=%E4%B8%AD%E6%96%87'
print(unquote(url))
