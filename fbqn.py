#! /usr/bin/env python
# coding:UTF-8
a = 0 
b = 1
n = int(input("请输入数字："))
while b < n:
    print(b,end=',')
    a,b = b,a+b

