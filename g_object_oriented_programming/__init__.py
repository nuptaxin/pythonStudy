#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' module comment '

__author__ = 'Ashin Ren'

std1={'name':'Ashin','score':80}
std2={'name':'John','score':90}

def print_score(std):
    print('%s:%s' % (std['name'],std['score']))

print_score(std1)

#定义一个类
class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def print_score(self):
        print('%s:%s' % (self.name,self.score))

ashin=Student('Ashin Ren',99)
ashin.print_score()