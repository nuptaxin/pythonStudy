#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#初始化dict
d={'axin':1,'john':2,'lina':3}
print(d)
print(d['axin'])
#新增或修改值
d['dyson']=4
print(d['dyson'])
#先判断值是否存在，然后取值
print(d.get('dyss'))
print(d.get('dyss'),-2)
if 'dyss' in d:
    print(d['dyss'])