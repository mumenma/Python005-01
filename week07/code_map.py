# 自定义一个 python 函数，实现 map() 函数的功能。

def square(x):
    return x **2

def funcLikcMap(func,list):
    return (func(i) for i in list )

m = map(square,range(10))
print(list(m))
print([square(x) for x in range(10)])
print(list(funcLikcMap(square,range(10))))