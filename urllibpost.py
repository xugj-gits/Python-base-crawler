# -*- coding: UTF-8 -*-
"""
POST 演示
"""
import urllib

# 设置参数
params = {'word':'hello'}
#通过bytes(urllib.parse.urlencode())将post数据进行转换
data = bytes(urllib.parse.urlencode(params), encoding='utf-8')
url = 'http://httpbin.org/post'
response = urllib.request.urlopen(url, data)
print(response.read())