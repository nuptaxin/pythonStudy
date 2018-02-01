#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from abstest import mytest
import math
#定义一个函数
def my_abs(x):
    if x>0:
        return x
    elif x==0:
        return
    else:
        return -x
print(my_abs(-8))
print(my_abs(0))
print(mytest(-7))
#跳过当前函数（直接return None）
def my_pass(x):
    pass
#调用外部函数
print(my_pass(7))
#进行数据类型检查
def my_data_type(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x>=0:
        return x
    else:
        return -x
print(my_data_type(2))
#返回多个值
def move(x, y, step, angle=0):
    nx = x+step*math.cos(angle)
    ny = y+step*math.sin(angle)
    return nx,ny
x,y=move(100,100,60,math.pi/6)
t=move(100,100,60,math.pi/6)
print(x,y)
print(t)