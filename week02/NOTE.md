# 学习笔记
# osi 参考模型
## request比urllib更方便更简洁
## 文件操作
with open打开文件，用上下文，好处是会自动关闭文件，不用在finally里面close，之所以有这样的效果，是因为with的存在，调用了__enter__和__exit__两个魔术方法
## 异常
try except
捕获到异常，如果什么都不做，就用pass
抛出异常 raise 
所有的异常都是基于BaseException，但是要自己写一个异常的话，一定要继承Exception
## 魔术方法
## echo服务的作用
确定对应的微服务是否是存活的
## socket
## websocket

## http://httpbin.org 专门用于http的学习和调试的一个网站


