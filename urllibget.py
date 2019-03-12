# -*- coding: UTF-8 -*-
"""
GET方式演示
"""
import urllib

values = {}
values['wd'] = 'word'
data = urllib.parse.urlencode(values)
url = 'http://www.baidu.com/s'
getUrl = url + '?' + data
print(getUrl)
response = urllib.request.urlopen(getUrl)
print(response.read())
