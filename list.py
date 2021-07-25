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


#列表方法
a = [66.25,333,333,1,1234.5]

#count方法返回元素在列表中出出现的次数
print(a.count(333))

#insert方法向列表指定位置添加元素
a.insert(2,-1) #在位置2处添加元素-1
print(a)
#append方法向列表末尾添加元素
a.append(333)
print(a)

#index方法返回元素出现的第一个位置
print(a.index(333))

#remove方法删除列表中元素，如果有多个相同元素则删除第一个位置最靠前的一个
a.remove(333)
print(a)

#reverse方法倒排列表里的元素
a.reverse()
print(a)
#sort方法按照从小到大的顺序将列表进行排序
a.sort()
print(a)


#将列表当栈使用
b= [2,3,4]
b.append(5)
b.append(6)
print(b)
print(b.pop())
print(b.pop())
print(b.pop())
print(b)


#列表推导式
vec = [2,4,6]
print([3*x for x in vec])

print([[x,x**2] for x in vec])

#过滤
print([3*x for x in vec if x > 3])

c= [2,4,6]
d= [4,3,-9]
print([x*y for x in c for y in d])
print([x+y for x in c for y in d])
print([c[i]*d[i] for i in range(len(c))])
