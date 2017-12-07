#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#for循环
li = [4,5,6]
for x in li:
    print(x)
#range()函数
for x in range(5):
    print(x)
#while循环
m = 0
while m <10:
    m=m+1
    print(m)
print('end',m)
#break
m = 5
while m<100:
    m=m+2
    if m>7:
        break
print(m)
#continue
n=3
while n<20:
    n=n+3
    if n<10:
       continue
    print('ppp:',n)
