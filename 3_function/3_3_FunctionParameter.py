#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#位置参数（使用递归）
def power(x,n):
    if n>1:
        return power(x, n - 1)*x
    else:
        return x
#位置参数
def power1(x,n):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s
#默认参数
def power2(x,n=2):
    if n>1:
        return power(x, n - 1)*x
    else:
        return x
#选择性使用默认参数
def power3(x,n=2,q='m'):
    if q!='m':
        print(q)
    if n>1:
        return power(x, n - 1)*x
    else:
        return x

print(power1(5,4))
print(power2(5))
print(power3(5,q='t'))

#定义可变参数
#普通函数的使用
def calc(num):
    s=0
    for x in num:
        s=s+x*x
    return s
print('可变参数：',calc([1,2,3]))
#加*变为可变参数函数
def calc(*num):
    s=0
    for x in num:
        s=s+x*x
    return s
print('可变参数2：',calc(1,2,3,4))
#传入一个list或tuple
t=(1,2,3,4)
print('可变参数2：',calc(*t))

#关键字参数，比如注册时可以注册多余的信息，而函数可以写的很简洁
def person(name,age,**kw):
    print('name:',name,',age:',age,',other:',kw)
person('axin',26,city='beijing',job='engineer')
d={'city':'Nanjing','job':'engineer'}
person('axin1',27,**d)

#命名关键字参数
def person1(name,age,*,city):
    print('name:', name, ',age:', age, ',other:', city)
person1('axin',26,city='beijing')
#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def person2(name,age,*args,city,job):
    print(name,age,args,city,job)
person2('aaa',26,city="NJ",job="EN")
