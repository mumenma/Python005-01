#实现一个 @timer 装饰器，记录函数的运行时间，注意需要考虑函数可能会接收不定长参数。
# import datetime
import time
from functools import wraps

def timer(func):
    # print("1")
    @wraps(func) # 为了让下边调用的func方法是本身的func方法  ？？？疑问，是不是本身的方法究竟有什么区别，除了看对应的方法，在实际应用上会有什么不同
    def inner(*args,**kwargs):
        startTime = time.time()
        # print("2")
        ret = func(*args,**kwargs)
        # print("5")
        endTime = time.time()
        print(endTime - startTime )
        return ret
    # print("3")
    return inner

@timer
def func(a,b):
    print(a+b)
    time.sleep(0.1)
    #print("4")

if __name__ == "__main__":
    func(1,2)