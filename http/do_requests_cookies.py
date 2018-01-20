import requests

cookies ='d_c0="CCBCkGag0wyPThgjJHrJHw8y08CSK4qqPio=|1513140440"; _zap=efe56dc6-0ee3-476a-9489-ef392efe902c; __utmv=51854390.100-1|2=registration_date=20160103=1^3=entry_date=20160103=1; _xsrf=c884a34a2382e298aae09788040cd105; q_c1=23084462174740a4955d82f1985f51bf|1515771761000|1513140447000; __utmz=51854390.1515918108.19.15.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/topic/19553534/organize; aliyungf_tc=AQAAAD8MPlcc4AoASDuUtp94NWR9enGH; _xsrf=c884a34a2382e298aae09788040cd105; __utma=51854390.959339133.1513140449.1515918108.1516265045.20; __utmc=51854390; capsion_ticket="2|1:0|10:1516271951|14:capsion_ticket|44:M2E3NDdiNTAyNjFlNDZkNzkzMjc5MDhiOTY4ZTZhYzI=|639e5d4db4dc6bca232853869749ab4120ba027dcea90a132f5520d7e8275309"; z_c0="2|1:0|10:1516271967|4:z_c0|92:Mi4xSHRsd0FnQUFBQUFBRUVLUVpxRFREQ2NBQUFDRUFsVk5Yd2FJV2dBQXhaejVlQ3hTZlpqUHJXTkdDYjNNb00xYk1n|4efbd452995728960ea04dbe644574f8cc00a422446e9b570bbd24c00db0654f"'
jar = requests.cookies.RequestsCookieJar()
headers = {
    'Host':'www.zhihu.com',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

for cookie in cookies.split(';'):
    key, value = cookie.split('=',1)
    jar.set(key, value)

r = requests.get('https://www.zhihu.com', cookies=jar, headers=headers)
print(r.text)
