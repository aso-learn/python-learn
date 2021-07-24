#! /usr/bin/env python3
#coding:utf-8
list1 = ['a','b','c','d','e']
list2 = [1,2,3,4,5]
print(list1[0])
print(list2[1:4])
list2[2] = 6
print(list2[2])
del list2[0]
print(len(list2))
print(list2)
print(list1+list2) #两个列表组合
print(list1*2) #重复输出两次list1[]
print(4 in list2) #判断4在不在list2[]中
