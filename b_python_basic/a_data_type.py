#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#整数除法(结果一定是精确的)、地板除和取余
print('整数除法：')
print(10/3)
print(10//3)
print(10%3)
#对于很大或者很小的浮点数使用科学计数法，把10用e代替=>12.3e8=12.3*10^8
print('浮点数：', 1.23e8)
#字符串及转义
print('字符串：')
print('\thello\\\tpython')
print(r'\t\n\\')
print('''uuu\n
iiii
pppp''')
print(r'''uuu\tkk
fff''')
#布尔值，布尔值只有True、False（注意首字母大写），布尔值可以用and or not运算
print('布尔值：', not True)
#空值（不可理解为0）
print('空值：', None)
#变量，变量是指向性的作用
print('变量：')
a='AAA'
b=a
a='BBBB'
print(b)
#常量，通常用全大写变量名来定义常量
PI = 3.14159265359
#数据类型转换
a='967'
print(int(a))
print(float(a))
print(bool(a))
print(hex(13))