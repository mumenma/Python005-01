import requests
import sys

url = "https://www.zhihu.com/question/51903374"

ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
header = {'user-agent':ua}   # 模拟浏览器的头部

try:
    response = requests.get(url, headers=header)
except requests.exceptions.ConnectTimeout as e :
    print(f"requests库超时")
    sys.exit(1)


print(response.text)