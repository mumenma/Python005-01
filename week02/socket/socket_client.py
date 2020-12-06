import socket
from pathlib import Path

# AF_INET 表示IPV4地址， SOCK_STREAM表示TCP谢意
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print(f"s1:{s}")

host = "localhost"#要连接的主机
port = 9999#要连接的接口

s.connect((host,port))

#s.sendall()

buffer = []
while True:
    data = s.recv(1024)
    if data:
        # print(data.decode('utf-8'))
        buffer.append(data)
    else:
        break

s.close()

response = b''.join(buffer)

# header, html = response.split(b'\r\n', 1)

pathName = str(Path(__file__).parent) + "/save_add.png"
with open(pathName,'wb') as f:
    f.write(response)
