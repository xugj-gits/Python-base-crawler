# -*- coding: UTF-8 -*-

import urllib.request

# 构建了代理Handler
proxy_handler = urllib.request.ProxyHandler({
    'http':'http://163.125.221.128:8119/'
})

# 创建自定义opener对象
opener = urllib.request.build_opener(proxy_handler)
response = opener.open('http://httpbin.org/get', timeout=2)
print(response.read())