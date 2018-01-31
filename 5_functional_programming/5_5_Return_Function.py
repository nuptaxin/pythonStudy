#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def lazy_sum(*args):
    def sum():
        ax=0
        for n in args:
            ax=ax+n
        return ax
    return sum
f=lazy_sum(1,2,3,4,5)
print(f)
print(f())

#每次调用函数时都会返回一个新的函数，及时传入相同的参数
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1==f2)

#慎用返回函数时的内部变量
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1(),f2(),f3())
#原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9
#返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

#修改后的函数
def count1():
    def f(i):
        def g():
            return i*i
        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs
f1, f2, f3 = count1()
print(f1(),f2(),f3())

#调用是f(i)函数为立即执行，所以绑定到g()的参数就不会改变了
