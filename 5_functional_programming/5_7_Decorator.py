#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def now():
    print('2018-01-31')

now()
print(now.__name__)

#定义装饰器（由于任何函数的参数都可以用*args, **kw表示，所以该值可以代表任意函数的任意参数）
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

#借助Python的@语法，把decorator置于函数的定义处
@log
def now1():
    print('2018-01-31')

now1()
#上述调用相当于执行了以下语法
log(now)()

#自定义带文本的装饰器
def log2(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log2('execute')
def now2():
    print('2015-3-25')

now2()
print(now2.__name__)

#把原始函数的__name__等属性复制到新函数中
import functools
def log3(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log3('execute')
def now3():
    print('2015-3-25')

now3()
print(now3.__name__)
