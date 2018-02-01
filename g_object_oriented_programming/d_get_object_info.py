#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' module comment '

__author__ = 'Ashin Ren'

#使用type()
print(type(123))
print(type('str'))
print(type(None))

#如果一个变量指向函数或类，也可以用type()判断：
print(type(abs))
class Animal(object):
    pass
print(type(Animal()))

#type返回的类型
print(type(123)==type(456))
print(type(123)==int)

#判断一个对象是否是函数
import types
def fn():
    pass
print('函数判断类型：',type(fn)==types.FunctionType)
print('系统函数判断类型：',type(abs)==types.BuiltinFunctionType)
print('lambda函数判断类型：',type(lambda x:x)==types.LambdaType)
print('生成器函数判断类型：',type((x for x in range(10)))==types.GeneratorType)


#使用isinstance()
class Dog(Animal):
    pass
class Husky(Dog):
    pass
a=Animal()
d=Dog()
h=Husky()
print(isinstance(h,Husky))
print(isinstance(h,Dog))

#使用isinstance()对基本类型做判断
print('基本类型判断1：',isinstance('a',str))
print(isinstance(5,int))

#判断一个变量是否是某些类型中的一种
print(isinstance([1,2,3],(list,tuple)))


#使用dir()获取一个对象所有的属性和方法
class MyDog(object):
    def __init__(self):
        self.m=9
    def fn(self):
        return 89
md=MyDog()
print(dir(md))
print(dir('ABC'))
print('ABC'.__len__())
print(hasattr(md,'m'))
print(setattr(md,'m',19))
print(getattr(md,'m',404))
print(getattr(md,'m1',404))

#获取对象的方法
print('获取对象的方法',hasattr(md,'fn'))
f=getattr(md,'fn')
print(f)
print(f())

