#!/usr/bin/env python3
# -*- coding: utf-8 -*-
d={'a':1,'b':2,'c':3}
for key in d:
    print('key:',key)

for value in d.values():
    print('value:',value)

for k,v in d.items():
    print('key:',k,',value:',v)

#迭代字符串
for ch in 'ABC':
    print(ch)

#判断是否为可迭代对象
from collections import Iterable
print(isinstance('abc',Iterable))

#下标迭代
for i,value in enumerate(['a','B','c']):
    print('下标：',i,',值：',value)