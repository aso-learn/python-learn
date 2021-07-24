#! /usr/bin/env python3
# coding:UTF-8
var1 = 'hello world' #变量赋值
var2 = 'quanxin' 
print(var1) #打印输出变量var1
print(var2) 
print(var1[2]) #输出变量var1中从左到右第三个字符
print(var2[2:6]) #输出变量var2中从左到右第三个到第六个字符串
print(var1[:6]+'python') #将变量var1中从第6个字符往后的字符修改为''里面的内容
print("line1\\line2") #\转义字符（可以理解为将特殊符号输出出来)在行尾相当于续行字符
print(var1+var2) #将两个变量里的字符串组合起来
print(var1*2) #将var1输出两次
if("h" in var1):
    print("var1变量里有h字母")
else:
    print("var1里没有字母h")
    
print(r'\n') #将''里的全部元素原样输出

print("我叫 %s 今年 %d 岁" % ('小明',10)) #字符串格式化

print("""这是
多行
字符串
tab(\t)
换行符[\n]
""")

