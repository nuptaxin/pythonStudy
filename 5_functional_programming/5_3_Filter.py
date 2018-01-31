#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#删除list中的所有偶数，只保留奇数
def is_odd(n):
    return n%2==1
print(list(filter(is_odd,list(range(20)))))

#删除掉序列中的空字符
def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty,['',' ','A',None,'xx'])))

#使用filter求素数
#创建一个生成器
def _odd_iter():
    n=1
    while True:
        n=n+2
        yield n
#该函数返回的是一个函数，过滤所有除以当前值后为0的那些值
def _not_divisible(n):
    return lambda x:x%n>0

#定义最终的函数，从生成器中取数，并且依次过滤掉当前值的倍数
def primes():
    yield 2
    it=_odd_iter()
    while True:
        n=next(it)
        yield n
        it = filter(_not_divisible(n),it)
for n in primes():
    if n<1000:
        print(n)
    else:
        break


