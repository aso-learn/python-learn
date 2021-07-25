#! /usr/bin/env python
#coding:UTF-8
#函数
#输出hello world!
def hello():
    print("helloworld!")
hello()

#比较大小
def num(a,b):
    if a>b:
        return a
    else:
        return b
a = 4
b = 5
print(num(a,b))

#计算矩形面积
def area(h,w):
    return h*w
print(area(5,10))
