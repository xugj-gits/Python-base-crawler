# -*- coding:UTF-8 -*-

from urllib import request, error

try:
    response = request.urlopen('http://pythonsite.com/1111.html')
except error.URLError as e:
    print(e.reason)

try:
    response = request.urlopen('http://pythonsite.com/1111.html')
except error.HTTPError as e:
    print(e.reason)
    print(e.code)
    print(e.headers)