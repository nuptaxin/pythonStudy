#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#创建一个set
s=set([1,2,3])
print(s)
#添加元素
s.add(4)
print(s)
#删除元素
s.remove(2)
print(s)
#删除任意一个元素
s.pop()
print(s)
#交集、并集操作
s1=set([1,2,3])
s2=set([3,6])
print(s1&s2)
print(s1|s2)
#把tuple放入set
li=[3,6]
t=(2,4)
s=set([t])
print('xxx',s)
