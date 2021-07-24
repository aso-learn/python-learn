#! /usr/bin/env python3
#coding:UTF-8

#break 
n = 5
while n>0:
    n-=1
    if n ==2:
        break
    print(n,end=",")
print("end")
#当n=2的时候终止循环

#continue

m = 5
while m>0:
    m-=1
    if m==2:
        continue
    print(m,end=",")
print("end")
#当m=2时跳过这一次循环，输出结果 是4 3 1
