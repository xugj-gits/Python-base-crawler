# -*- coding:UTF-8 -*-

# urllib.request 请求模块
# import urllib.request
# import urllib.parse
# 以上2个导入可以合并为
from urllib import request, parse
import ssl

content = ssl._create_unverified_context()

url = 'https://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'httpbin.org'
}
params = {
    'name': '高效码农'
}

data = bytes(parse.urlencode(params), encoding='utf8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
response = request.urlopen(req, context=content)
print(response.read())