#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' module comment '

__author__ = 'Ashin Ren'

#设置类中的私有变量
class Student(object):
    def __init__(self,name,score,grade):
        self.__name=name
        self.__score=score
        self._grade=grade
    def print_score(self):
        print('%s:%s-%s' % (self.__name,self.__score,self._grade))

ashin = Student('Ashin',97,'三')
ashin.print_score()
#访问限制:单下划线可以访问，但是不建议访问；双下划线python内部将其改为_类名__属性名,也不建议直接访问(get,set方法)
print(ashin._grade)
print(ashin._Student__name)