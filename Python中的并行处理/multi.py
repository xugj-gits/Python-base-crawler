import multiprocessing as mp
from numpy import random
import time

# 准备数据
random.seed(100)
arr = random.randint(0, 10, size=[20000, 5])
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
endtime = time.time()

print(results[:10])
print('花费时间：', endtime - start)
