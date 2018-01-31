#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#map的使用
def f(x):
    return x*x
r=map(f,list(range(10)))
print(list(r))

#reduce的使用
def add(x,y):
    return x+y
from functools import reduce
r=reduce(add,list(range(4)))
print(r)

#自定义字符串转int函数
from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2num(s):
    return DIGITS[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))

print(str2int('376552'))