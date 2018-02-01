#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#判断一个对象是否是Iterable对象
from collections import  Iterable
print(isinstance([],Iterable))
print(isinstance({},Iterable))

#判断一个对象是否是Iterator
from collections import  Iterator
print(isinstance([],Iterator))
print(isinstance((x for x in range(10)),Iterator))

#将一个Iterable对象转换为Iterator对象
print(isinstance(iter([]),Iterator))