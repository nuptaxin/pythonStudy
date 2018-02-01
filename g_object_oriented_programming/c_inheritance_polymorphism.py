#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' module comment '

__author__ = 'Ashin Ren'

#定义父类Animal
class Animal(object):
    def run(self):
        print('Animal is running……')
#定义子类Dog和Cat
class Dog(Animal):
    pass
class Cat(Animal):
    pass
animal=Animal()
animal.run()
dog=Dog()
dog.run()
cat=Cat()
cat.run()

#子类重写父类的方法
class Dog1(Animal):
    def run(self):
        print('Dog1 is running...')
class Cat1(Animal):
    def run(self):
        print('Cat1 is running...')
dog=Dog1()
dog.run()
cat=Cat1()
cat.run()

#多态：判断对象的类型试试
print(isinstance(dog,Dog1))
print(isinstance(cat,Cat1))
print(isinstance(dog,Animal))

#定义函数run_twice
def run_twice(animal):
    animal.run()
    animal.run()

run_twice(animal)
run_twice(dog)
run_twice(cat)

#新增一种类
class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')

run_twice(Tortoise())

#动态语言的特殊性--不继承Animal，定义一个有run()方法的类
class Timer(object):
    def run(self):
        print('Timer start...')
run_twice(Timer())
