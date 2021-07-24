#! /usr/bin/env python3
# coding；UTF-8
#if猜字谜游戏
number = 7
g = -1
while g != number:
    g = int(input("请输入数字："))
    if g == number:
        print("猜对了")
    elif g<number:
        print("太小了")
    elif g>number:
        print("太大了")

