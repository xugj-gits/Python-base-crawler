# -*- coding:UTF-8 -*-

import re

pattern = re.compile(r'world')

resutl1 = re.search(pattern, 'hello wor1ld!')
resutl2 = re.search(pattern, 'hello world!')

if resutl1:
    print(resutl1.group())
else:
    print('匹配失败❎')


if resutl2:
    print('匹配成功✅：' + resutl2.group())
else:
    print('匹配失败❎')