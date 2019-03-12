# -*- coding:UTF-8 -*-
from urllib.parse import urlparse,urlunparse,urlencode

# urlparse
result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(result)

# urlunparse
data = ['http','xugj520.cn', 'index.html', 'user','a=123','commit']
print(urlunparse(data))

# urlencode
params = {
    'name':'高效码农',
    'blog':'xugj520.cn'
}
base_url = 'https://xugj520.cn?'
url = base_url + urlencode(params)
print(url)
