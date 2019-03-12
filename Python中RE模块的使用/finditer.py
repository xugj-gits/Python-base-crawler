#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   finditer.py
@Time    :   2019/03/12 16:25:43
@Author  :   高效码农 
@Version :   1.0
@Contact :   514583562@qq.com
@License :   (C)Copyright 2019-2020, xugj520.cn
@Desc    :   None
'''

import re

pattern = re.compile(r'[\d]+')
for p in re.finditer(pattern, '这是1个测试finditer的123demo'):
    print(p.group())
