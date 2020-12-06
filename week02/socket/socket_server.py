import socket
from pathlib import Path

def open_server():
    # AF_INET 表示IPV4地址， SOCK_STREAM表示TCP谢意
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print(f"s1:{s}")

    host = "localhost"#要连接的主机
    port = 9999#要连接的接口

    #对象s绑定到指定的主机和端口上
    s.bind((host,port))
    #只接受1个连接
    s.listen(1)
    while True:
        conn, addr = s.accept()
        print(f'Connected by {addr}')
        pathName = str(Path(__file__).parent) + "/add.png"
        with open(pathName,"rb") as f:
            t = f.read()
            conn.sendall(t)
        conn.close()
    s.close()

if __name__ == '__main__':
    open_server()




