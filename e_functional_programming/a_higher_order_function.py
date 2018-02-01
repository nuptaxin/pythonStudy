#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#变量指向函数
f = abs
print(f(-32))

#函数名也是变量
print(abs)
abs=10
print(abs)

#传入函数
abs=f
def add(x,y,f):
    return f(x)+f(y)
print(add(-5,6,abs))