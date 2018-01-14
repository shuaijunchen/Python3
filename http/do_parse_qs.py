from urllib.parse import parse_qs

query = 'name=genmey&age=22'
print(parse_qs(query))
