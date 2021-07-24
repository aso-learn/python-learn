#! /usr/bin/env python3
# coding:utf-8
tup1 = (1,2,3,4,5,6)
tup2 = ("a","b","c","d","e")
tup3 = "f","g","h","i" #元组创建规则
tup4 = ("asd",) #元组只有一个元素的时候也要加,否则或认为是整型
print(type(tup4))
#元组里面的元素不允许被修改但是可以进行两个元组连接

del tup4
print(max(tup1))#输出tup1里面最大的元素
print(min(tup1))#输出最小元素

list = [1,2,3,4,5]
tup5 = tuple(list)
print(tup5)
print(type(tup5))

