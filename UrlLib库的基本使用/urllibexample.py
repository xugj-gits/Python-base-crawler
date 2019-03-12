# -*- coding：utf-8 -*-

import urllib

# urllib.request 请求模块
response = urllib.request.urlopen("http://www.baidu.com")
print(response.read())