# Ptyhon中RE模块的使用
<div align=center><img src="Python Re模块.png"/></div>

### 1. 正则表达式
参考：[廖雪峰的官方网站](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143193331387014ccd1040c814dee8b2164bb4f064cff000)

### 2. Python Re模块
Python提供re模块，包含所有正则表达式的功能。由于Python的字符串本身也用\转义，<font color=red>因此我们强烈建议使用Python的r前缀，就不用考虑转义的问题了</font>

###### 2.1 &ensp;&ensp;re.match(pattern, string[, flags])
>如果字符串开头的零个或多个字符与正则表达式模式匹配，则返回相应的匹配对象。None如果字符串与模式不匹配则返回; 请注意，这与零长度匹配不同。

>请注意，即使在多行模式下，re.match()也只会匹配字符串的开头而不是每行的开头。

```
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

```
参考：[Match API](https://docs.python.org/3.7/library/re.html?highlight=match#match-objects)

###### 2.2 &ensp;&ensp;re.search（pattern，string，flags = 0 ）
>扫描字符串，查找正则表达式模式产生匹配的第一个位置 ，并返回相应的match object.
如果字符串中没有位置与模式匹配则返回None;

```
# -*- coding:UTF-8 -*-

import re

pattern = re.compile(r'world')

resutl1 = re.search(pattern, 'hello wor1ld!')
resutl2 = re.search(pattern, 'hello world!')

if resutl1:
    print(resutl1.group())
else:
    print('匹配失败❎')


if resutl2:
    print('匹配成功✅：' + resutl2.group())
else:
    print('匹配失败❎')
```
运行结果：
> 匹配失败❎  
匹配成功✅：world

###### 2.3 &ensp;&ensp;re.split(pattern，string，maxsplit = 0，flags = 0)

> 按照能够匹配的子串将string分割后返回列表。maxsplit用于指定最大分割次数，不指定将全部分割。

```
import re

pattern = re.compile(r'\d+')

print(re.split(pattern, '这是1个测试split的demo'))
```
运行结果：
>['这是', '个测试split的demo']

###### 2.4 &ensp;&ensp;re.findall(pattern，string，flags = 0 )
> 以列表形式返回全部能匹配的子串。
```
import re

pattern1 = re.compile(r'\d+')
pattern2 = re.compile(r'[a-z]+')

print(re.findall(pattern1, '这是1个测试findall的123demo'))
print(re.findall(pattern2, '这是1个测试findall的123demo'))
```
运行结果：
> ['1', '123']
> ['findall', 'demo']

###### 2.5 &ensp;&ensp; re.finditer(pattern, string[, flags])

> 返回一个顺序访问每一个匹配结果（Match对象）的迭代器。
```
import re

pattern = re.compile(r'[\d]+')
for p in re.finditer(pattern, '这是1个测试finditer的123demo'):
    print(p.group())
```
运行结果：
> 1
> 123

###### 2.6 &ensp; &ensp; re.sub(pattern, repl, string[, count])
> 返回使用repl替换每一个匹配的字符串后的字符串

```
import re

pattern = re.compile(r'\d+')

print(re.sub(pattern, 'one', '这是101个测试sub函数的demo'))
```
运行结果：
> 这是one个测试sub函数的demo

###### 2.7 &ensp;&ensp; re.subn(pattern, repl, string[, count])
> 返回 (sub(repl, string[, count]), 替换次数)。
```
import re

pattern = re.compile(r'\d+')

print(re.subn(pattern, 'one', '这是101个测试subn函数的demo23456'))

# 也可以通过pattern.subn() pattern.match()等调用
print(pattern.subn('two', '这是101个测试subn函数的demo23456'))
```
运行结果：
> ('这是one个测试subn函数的demoone', 2)
> ('这是two个测试subn函数的demotwo', 2)


