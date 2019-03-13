# Python中的并行处理
并行处理是一种操作模式，其中任务在同一计算机中的多个处理器中同时执行。它旨在减少整体处理时间。

### 1.&ensp;&ensp;简介
并行处理是一种操作模式，其中任务在同一计算机中的多个处理器中同时执行。它旨在减少整体处理时间。

但是，在进程之间进行通信时通常会有一些开销，这实际上会增加小任务的总时间而不是减少它。

在python中，multiprocessing模块用于通过使用子进程（而不是线程）来运行独立的并行进程。它允许您利用计算机上的多个处理器（Windows和Unix），这意味着，这些进程可以在完全独立的内存位置运行。

### 2.&ensp;&ensp;你的电脑可以运行多少个最大并行进程？
你的电脑一次可以运行的最大进程数受计算机中处理器数量的限制。你可以用multiprocessing中的cpu_count()函数
```
>>> import multiprocessing as mp
>>> print(mp.cpu_count())
4
```
### 3.&ensp;&ensp;什么是同步和异步执行？
在并行处理中，有两种类型的执行：同步和异步。

同步执行是按照启动顺序完成的过程之一。这是通过锁定主程序直到相应的过程完成来实现的。

另一方面，异步不涉及锁定。结果，结果的顺序可能会混淆，但通常可以更快地完成。

multiprocessing实现函数的并行执行有两个主要对象：PoolClass和ProcessClass。

1. Pool 类
    + 1.1&ensp;&ensp; 同步执行
        + Pool.map() 和 Pool.starmap()
        + Pool.apply()

+ 2.&ensp;&ensp;异步执行
    + Pool.map_async() 和 Pool.starmap_async()
    + Pool.apply_async()）

+ 2.&ensp;&ensp;Process 类
让我们讨论一个典型的问题，并使用上述技术实现并行化。在本教程中，我们坚持使用Pool该类，因为它最方便使用并提供最常见的实际应用程序。

### 4.&ensp;&ensp;计算每行中给定范围之间存在的数量
给定2D矩阵（或列表列表），计算每行中给定范围之间存在的数量。

```
from numpy import random
import time

# 准备数据
random.seed(100)
arr = random.randint(0, 10, size=[200000, 5])
data = arr.tolist()
print(data[:5])
```

没有并行化的解决方案
```
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
```
> 输出：花费时间： 0.798130989074707

### 5.&ensp;&ensp;并行化解决问题
###### 5.1&ensp;&ensp;使用Pool.apply（）并行化
```
import multiprocessing as mp
from numpy import random
import time

# 准备数据
random.seed(100)
arr = random.randint(0, 10, size=[200000, 5])
data = arr.tolist()
# print(data[:5])


def howmany_within_range(row, minimun, maximum):
    count = 0
    for n in row:
        if minimun <= n <= maximum:
            count += 1
    return count


# Step 1: Init multiprocessing.Pool()
pool = mp.Pool(mp.cpu_count())

start = time.time()
# Step 2: `pool.apply` the `howmany_within_range()`
results = [pool.apply(howmany_within_range, args=(row, 4, 8)) for row in data]

# Step 3: Don't forget to close
pool.close()
pool.join()
endtime = time.time()

print(results[:10])
print('花费时间：', endtime - start)
```
>花费时间： 38.05518102645874

######5.2&ensp;&ensp; 使用Pool.map进行并行化
Pool.map()只接受一个iterable作为参数。因此，作为一种解决方法，我howmany_within_range通过设置默认值minimum和maximum参数来修改函数来创建一个新函数，因此它只接受一个可迭代的行列表作为输入。我知道这不是一个很好的用法，但它清楚地表明它与它的区别。
```
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
```
> 花费时间： 0.46733903884887695


