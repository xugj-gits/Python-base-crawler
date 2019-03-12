#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   findall.py
@Time    :   2019/03/12 16:06:18
@Author  :   高效码农 
@Version :   1.0
@Contact :   514583562@qq.com
@License :   (C)Copyright 2019-2020, xugj520.cn
@Desc    :   None
'''

import re

pattern1 = re.compile(r'\d+')
pattern2 = re.compile(r'[a-z]+')

print(re.findall(pattern1, '这是1个测试findall的123demo'))
print(re.findall(pattern2, '这是1个测试findall的123demo'))