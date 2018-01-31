#!/usr/bin/env python3
# -*- coding: utf-8 -*-

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0:3])
print(L[1:2])
print(L[-2:])
L = list(range(100))
print(L[:-2])
print(L[::5])

#tuple切片后的结果仍然是tuple
print((0, 1, 2, 3, 4, 5)[:3])

#字符串切片，按照字符切，结果仍然是字符串
print('ABCDEFG'[2:5])