#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   multi2.py
@Time    :   2019/03/13 18:06:09
@Author  :   高效码农 
@Version :   1.0
@Contact :   514583562@qq.com
@License :   (C)Copyright 2019-2020, xugj520.cn
@Desc    :   None
'''

import multiprocessing as mp
from numpy import random
import time

# 准备数据
random.seed(100)
arr = random.randint(0, 10, size=[200000, 5])
data = arr.tolist()
# print(data[:5])


def howmany_within_range_rowonly(row, minimum=4, maximum=8):
    count = 0
    for n in row:
        if minimum <= n <= maximum:
            count = count + 1
    return count


# Step 1: Init multiprocessing.Pool()
pool = mp.Pool(mp.cpu_count())

start = time.time()
# Step 2: `pool.apply` the `howmany_within_range()`
# results = [pool.apply(howmany_within_range, args=(row, 4, 8)) for row in data]
results = pool.map(howmany_within_range_rowonly, [row for row in data])

# Step 3: Don't forget to close
pool.close()
endtime = time.time()

print(results[:10])
print('花费时间：', endtime - start)

