#! /usr/bin/env python3 
# coding:utf-8
dir1 = {'name':'python','years':'10','user':'quan'}
len(dir1)#输出字典里元素个数
print(dir1['name'])#输出键name的值python
dir1['years'] = 10#更改键years的值为数字10
dir1['age'] = 8#新增键age,键值为8
print(dir1)
del dir1['user']#删除user键和键值
print(dir1)
dir1.clear()  #清空整个字典
print(dir1)
del dir1 #删除字典
tup = (1,2,3,4)
dir2 = {tup[0]:12,'a':'abc',5:567}#字典里的键可以是数字、字符串、元组
print(dir2)

