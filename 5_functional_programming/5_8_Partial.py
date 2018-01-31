#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#字符串转数字函数
print(int('12345'))
#提供默认是10的base
print(int('10010',base=2))

#如果需要大量的转换，可以新定义函数
def int2(x,base=2):
    return int(x,base)

#也可以使用偏函数定义
import functools
int2p=functools.partial(int,base=2)

print(int('1000'))
print(int2p('1000'))

#max等使用偏函数时，会自动把*args加到左边
max2=functools.partial(max,10)
print(max2(2,3,4))