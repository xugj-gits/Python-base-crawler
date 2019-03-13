#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   matrix.py
@Time    :   2019/03/13 16:35:40
@Author  :   高效码农 
@Version :   1.0
@Contact :   514583562@qq.com
@License :   (C)Copyright 2019-2020, xugj520.cn
@Desc    :   None
'''

from numpy import random
import time

# 准备数据
random.seed(100)
arr = random.randint(0, 10, size=[200000, 5])
data = arr.tolist()
# print(data[:5])


def howMany_within_range(row, minimun, maximum):
    count = 0
    for n in row:
        if minimun <= n <= maximum:
            count += 1
    return count


result = []
start = time.time()
for row in data:
    result.append(howMany_within_range(row, minimun=4, maximum=8))

print(result[:10])
endtime = time.time()
print('花费时间：', endtime - start)
