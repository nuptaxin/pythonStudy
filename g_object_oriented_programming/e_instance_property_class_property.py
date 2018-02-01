#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' module comment '

__author__ = 'Ashin Ren'

class Student(object):
    #定义类属性
    name='Student'
    def __init__(self,name,age):
        self.name=name
        self.age=age

s=Student('Ashin',24)
#如果有相同的实例属性和类属性，调用实例的属性，实例属性将覆盖掉类属性
print(s.name)
#直接打印类属性
print(Student.name)
#删除类属性
del s.name
#再次调用实例的属性，将显示类属性
print(s.name)

