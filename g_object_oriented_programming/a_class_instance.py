#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' module comment '

__author__ = 'Ashin Ren'

#定义一个类（类后跟着的object表示该类从哪个类继承下来，默认使用object即可）
class Student(object):
    pass
bart=Student()
print(bart)
print(Student)

#自由的给实例绑定属性（不需要在类中定义）
bart.name='Ashin Ren'
print(bart.name)

#使用__init__强制把必须绑定的属性填写进去
class Student1(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score

#使用__init__强制指定属性后，在初始化对象
#bart=Student1() 不指定属性会报错
bart=Student1('Ashin',33)
#可以直接调用__init__中定义的self字段
print('name:',bart.name)


#数据封装：可以通过定义类中的函数来访问类中的数据
class Student2(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def print_score(self):
        print('%s:%s' % (self.name,self.score))

ashin=Student2('Ashin',55)
#外部代码修改内部name属性
ashin.name='xxx'
ashin.print_score()