#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   sub.py
@Time    :   2019/03/12 16:39:15
@Author  :   高效码农 
@Version :   1.0
@Contact :   514583562@qq.com
@License :   (C)Copyright 2019-2020, xugj520.cn
@Desc    :   None
'''

import re

pattern = re.compile(r'\d+')

print(re.sub(pattern, 'one', '这是101个测试sub函数的demo'))