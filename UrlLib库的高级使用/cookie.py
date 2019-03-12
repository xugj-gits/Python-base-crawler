# -*_ coding:UTF-8 -*-

import http.cookiejar, urllib.request

# 创建一个CookieJar类
cookie = http.cookiejar.CookieJar()
# HTTPCookieProcessor
handler = urllib.request.HTTPCookieProcessor(cookie)
# 创建一个OpenerDirector类
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
for item in cookie:
    print(item.name+"="+item.value)