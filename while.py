#! /usr/bin/env python3
# coding:UTF-8
#while
num =1
n = 0
while num<=100:
    n+=num
    num+=1
print(n)

#while..else..
m = 0 
while m<5:
    print(m,"<5",end=" ")
    m+=1
else:
    print("m>=5")


#无限循环
#while 1:print("true")

#for循环遍历
list = [1,2,3,4,5]
for i in list:
    print(i,end=" ")

#for break
list2 = [1,2,3,4,5,6]
for o in list2:
    if o == 5:
        print("我是5")
        break
    print(o,end=",")
else:
    print("没有数据")
print("over")


#range()函数，生成数列
for p in range(10):#从0开始到9结束
    print(p,end=",")
print('\n')
for u in range(3,7):#生成从3到6的列表
    print(u,end=",")
print('\n')
for y in range(1,10,2):
    print(y,end=",")


