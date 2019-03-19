#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test1.py
@Time    :   2019/03/19 17:45:53
@Author  :   高效码农 
@Version :   1.0
@Contact :   514583562@qq.com
@License :   (C)Copyright 2019-2020, xugj520.cn
@Desc    :   None
'''

from PyVaildTool import PyVaildTool


class test1:
    IdCard = '130529198809230034'
    print(PyVaildTool.vaildIDCard(IdCard))