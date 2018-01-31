#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#使用匿名函数
t=list(map(lambda x:x*x,[1,2,3,4,5,6,7,8,9]))
print(t)

#把匿名函数赋值给一个变量
f = lambda x: x * x
print(f)

#把匿名函数作为返回值
def build(x, y):
    return lambda: x * x + y * y
print(build(2,3)())