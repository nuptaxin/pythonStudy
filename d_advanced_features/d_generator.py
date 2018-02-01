#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#创建一个生成器
g=( x*x for x in range(10))
print(g)
print(next(g))
print(next(g))
for n in g:
    print(n)

#在函数中定义yield来创建生成器
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
for n in fib(6):
    print(n)

#取到return返回的值：
g=fib(6)
while True:
        try:
            x = next(g)
            print('g:', x)
        except StopIteration as e:
            print('Generator return value:', e.value)
            break

