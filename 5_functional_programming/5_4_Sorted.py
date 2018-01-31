#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print(sorted([36,5,-12,9,21]))

#按key排序
print(sorted([36,5,-12,9,21],key=abs))

#将字母大小写转换后再排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))

#反向排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower,reverse=True))