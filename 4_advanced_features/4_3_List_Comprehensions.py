#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#生成从1~10的数字list
print(list(range(1,11)))
#生成[1x1, 2x2, 3x3, ..., 10x10]
print([x*x for x in range(1,11)])
#还可以加上if判断
print([x*x for x in range(1,11) if x%2==0])
#使用两层循环
print([m+n for m in 'ABC' for n in 'XYZ'])

#一行列出当前目录下的所有文件及目录
import os
print([d for d in os.listdir('.')])

#使用多个变量
d={'a':1,'b':2,'c':3}
print([k+'='+str(v) for k,v in d.items()])

#list中的所有大写变小写
l=['Allen','Tom','Jack']
print([d.lower() for d in l])