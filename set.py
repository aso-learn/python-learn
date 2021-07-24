#! /usr/bin/env python3
# coding:UTF-8
#创建集合的两种方法,{}和set()都能创建，但是创建空集合就必须使用set(),因为使用{}创建空集合会被认为是空字典！
set1 = {'a','b',1,2,3}
set2=set(('quan','xin'))

#集合之间的运算
a = {'dawdfaffasdafea'}
b = {'daasfesfawdeafafaf'}
print(a)
print(a-b) #集合a有b没有的元素
print(a | b) #a和b中包含的所有元素
print(a&b) #a和b的交集
print(a^b) #a有b没有和b有a没有的元素

#添加元素
c = {'quan','xin'}
c.add('python')
print(c)
c.update({1,2,3},[8,7])
print(c)
print(len(c)) #计算元素个数

#移除元素
c.remove(3) #如果元素不存在会发生错误
c.discard(2) #如果元素不存在也不会报错
print(c)
c.pop() #删除随机元素
print(c)
c.clear() #清空集合
print(c)

d = {'adwdawdawdawdwafaaxc'}
print('a' in d)

