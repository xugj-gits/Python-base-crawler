# -*- coding: UTF-8 -*-
import re

# 将正则表达式编译成Pattern对象，注意hello前面的r的意思是“原生字符串”
pattern = re.compile(r'hello')

# 使用re.match匹配字符串，获得匹配结果，无法匹配返回None
result1 = re.match(pattern, 'hello!hello3')
result2 = re.match(pattern, 'helloo xugj!')
result3 = re.match(pattern, 'helo xugj!')
result4 = re.match(pattern, '888hello xugj!')

print(result1) # 返回的是：a Match object 

# 匹配result1
if result1:
    print(result1.group())
else:
    print(result1)
    print('1匹配失败')


# 匹配result2
if result2:
    print(result2.group())
else:
    print(result2)
    print('2匹配失败')


# 匹配result3
if result3:
    print(result3.group())
else:
    print(result3)
    print('3匹配失败')


# 匹配result4
if result4:
    print(result4.group())
else:
    print(result4)
    print('4匹配失败')