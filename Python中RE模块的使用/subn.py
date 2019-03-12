#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   subn.py
@Time    :   2019/03/12 16:43:21
@Author  :   高效码农 
@Version :   1.0
@Contact :   514583562@qq.com
@License :   (C)Copyright 2019-2020, xugj520.cn
@Desc    :   None
'''

import re

pattern = re.compile(r'\d+')

print(re.subn(pattern, 'one', '这是101个测试subn函数的demo23456'))

# 也可以通过pattern.subn() pattern.match()等
print(pattern.subn('two', '这是101个测试subn函数的demo23456'))