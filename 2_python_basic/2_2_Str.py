#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#ord()获取字符的整数表示，chr()把编码转换为对应的字符
print(ord('A'))
print(chr(66))
#使用16进制写中文
print('\u4e2d\u6587')
#使用encode()编码str为制定bytes
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
#使用decode()解码bytes为str
print(b'\xe4\xb8\xad'.decode('utf-8'))
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))
#查看包含多少个字符
print(len('中文'))
print(len('中文'.encode('utf-8')))
#格式化输出
print('%02d-%d' % (7, 9))
print('%.3f' % 3.4)
#使用format格式化
print('hello , {0}成绩提升了{1:.2f}'.format('信', 16.3))
#replace(),本身为不可变值
a='abc'
b =a.replace('a','A')
print(b)
print(a)
