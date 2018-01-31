#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

print(fact(3))
#print(fact(1000))

#使用尾递归优化
def fact1(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
#print(fact1(1000))

#python中也没有做尾递归优化
