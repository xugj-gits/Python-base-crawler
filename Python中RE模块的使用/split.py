#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   split.py
@Time    :   2019/03/12 16:00:22
@Author  :   高效码农 
@Version :   1.0
@Contact :   514583562@qq.com
@License :   (C)Copyright 2019-2020, xugj520.cn
@Desc    :   None
'''
import re

pattern = re.compile(r'\d+')

print(re.split(pattern, '这是1个测试split的demo'))

