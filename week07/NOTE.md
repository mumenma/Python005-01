学习笔记
# 数据类型
## 按照是否可变分类
### 可变数据类型
列表 list
字典 dict
### 不可变数据类型
整形 int
浮点型 float
字符串型 string
元组 tuple
## 容器序列与扁平序列


# 拷贝和切片的结果
list1 = [1,2,3,4]
list2 = list(list1)
list3 = list1[:]
list1、list2、list3的内容是一样的，但是是三个不同的列表

# 拷贝
## 深拷贝
## 浅拷贝


# 数据类型的具体使用
[ i for i in range(1,11)]


# collections 官方文档：
https://docs.python.org/zh-cn/3.7/library/collections.html

# 函数的可变长参数
偏函数
# 高阶函数 和 lambda表达式
### lambda表达式
k = lambda x:x+1 
print(k(1))
### 高阶函数
#### map
#### reduce
from functools import reduce
#### filter
#### 偏函数
funtools.partial
#### itertools
## 闭包
## 装饰器
### 内置装饰器


## 迭代器 yield

## 协程和线程
