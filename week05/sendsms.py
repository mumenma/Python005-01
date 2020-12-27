from datetime import time
import redis
import time

client = redis.Redis(host='127.0.0.1',password='yuehong890313')
# 在使用短信群发业务时，公司的短信接口限制接收短信的手机号，每分钟最多发送五次，请基于 Python 和 redis 实现如下的短信发送接口：
# 已知有如下函数：

def sendsms(telephone_number: int, content:str, key=None):
    client.set(str(telephone_number),'0',nx=True) #nx为True则为了存在则不覆盖
    result = int(client.get(str(telephone_number)).decode())
    if result < 5:
        print("发送成功")
        client.incr(str(telephone_number))# +1
        client.set(str(telephone_number)+"_"+str(result + 1), str(int(time.time())))
    else:
        result = int(time.time()) - int(client.get(str(telephone_number)+"_"+str(1)).decode())
        if result < 60:
            print("1分钟内发送次数超过 5 次, 请等待 1 分钟")
        else:
            for i in range(1,5):
                client.set(str(telephone_number)+"_"+str(i), client.get(str(telephone_number)+"_"+str(i+1)).decode())
            client.delete(str(telephone_number)+"_"+str(5))
            sendsms(telephone_number,str,key)

#期望执行结果：
sendsms(12345654321, content='hello') # 发送成功
sendsms(12345654321, content='hello') # 发送成功
sendsms(12345654321, content='hello') # 发送成功
sendsms(12345654321, content='hello') # 发送成功
sendsms(12345654321, content='hello') # 发送成功
sendsms(88887777666, content='hello') # 发送成功
sendsms(12345654321, content='hello') # 1 分钟内发送次数超过 5 次, 请等待 1 分钟
sendsms(88887777666, content='hello') # 发送成功

# result = client.get('key')
# client.append('key','value4')
# result = client.get('key')
# print(result.decode())
# client.set('key2','100')
# client.decr('key2')#-1
# result3 = client.get('key2')
# print(result3.decode())

# print(client.keys()) #bytes类型

# for key in client.keys():
#     # print(key.decode())#输出转换出来的字符串
#     client.delete(key)

