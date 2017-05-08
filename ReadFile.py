#coding:utf-8
'''
Created on 2016-05-22

@author: Charlie
'''
import fileinput

file = open("D:\season_1\training_data\order_data\order_data_2016-01-01")             # 返回一个文件对象

line = file.readline()             # 调用文件的 readline()方法
while line:
    print line,                 # 后面跟 ',' 将忽略换行符
    # print(line, end = '')　　　# 在 Python 3中使用
    line = file.readline()

file.close()
#也可以写成以下更简洁的形式

for line in open("foo.txt"):
    print line,
#更详细的文件按行读取操作可以参考：http://www.cnblogs.com/xuxn/archive/2011/07/27/read-a-file-with-python.html


#1. 最基本的读文件方法：
# File: readline-example-1.py
 
while 1:
    line = file.readline()
    if not line:
        break
    pass # do something
#一行一行得从文件读数据，显然比较慢；不过很省内存。
#在我的机器上读10M的sample.txt文件，每秒大约读32000行
#2. 用fileinput模块

# File: readline-example-2.py
 
for line in fileinput.input("sample.txt"):
    pass
#写法简单一些，不过测试以后发现每秒只能读13000行数据，效率比上一种方法慢了两倍多……
#3. 带缓存的文件读取
# File: readline-example-3.py
 
while 1:
    lines = file.readlines(100000)
    if not lines:
        break
    for line in lines:
        pass # do something
#这个方法真的更好吗？事实证明，用同样的数据测试，它每秒可以读96900行数据！效率是第一种方法的3倍，第二种方法的7倍！

#在Python 2.2以后，我们可以直接对一个file对象使用for循环读每行数据：
# File: readline-example-5.py
 
for line in file:
    pass # do something
#而在Python 2.1里，你只能用xreadlines迭代器来实现：
# File: readline-example-4.py
 
 
for line in file.xreadlines():
    pass # do something