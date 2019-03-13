#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   actual01.py
@Time    :   2019/03/12 17:38:56
@Author  :   高效码农 
@Version :   1.0
@Contact :   514583562@qq.com
@License :   (C)Copyright 2019-2020, xugj520.cn
@Desc    :   None
'''
from urllib import request, error
import ssl
import re

content = ssl._create_unverified_context()

page = 1
url = 'https://www.qiushibaike.com/hot/page/' + str(page)
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'www.qiushibaike.com'
}

try:
    req = request.Request(url=url, headers=headers)
    response = request.urlopen(req, context=content)
    html = response.read().decode('UTF-8')
    pattern = re.compile('<div.*?content">.*?<span>.*?(.*?)</span>.*?</div>', re.S)
    paragraphs = re.findall(pattern, html)
    print(type(paragraphs))
    for paragraph in paragraphs:
        print(paragraph)

except error.HTTPError as e:
    if hasattr(e, 'code'):
        print(e.code)
    if hasattr(e, 'reason'):
        print(e.reason)

