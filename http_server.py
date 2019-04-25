"""
http server 1.0
接受浏览器请求
将固定的网页发送给浏览器

"""
from socket import *

#处理客户端请求
def handle_request(connfd):
    """

    :param connfd:
    :return:
    """
    #getpeername()     获取连接套接字
    print("Request from:",connfd.getpeername())
    request=connfd.recv(4096)       #接受请求request
    print(request)
    #获取请求行
    request_lines=request.splitlines()
    for line in request_lines:
        print(line)

    #返回固定网页给浏览器
    try:
        f=open('index.html')
    except IOError:
        response="HTTP/1.1 404 Not Found\r\n"
        response+='\r\n'
        response+='==Sorry not found=='
    else:
        response = "HTTP/1.1 200 OK\r\n"
        response += '\r\n'
        response += f.read()
        f.close()
    finally:
        #将结果给浏览器
        connfd.send(response.encode())
#创建套接字
def main():
    """

    :return:
    """
    sockfd=socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(('0.0.0.0',8900))
    sockfd.listen(3)
    print("listen the port 8900.....")
    while True:
        connfd,addr=sockfd.accept()
        handle_request(connfd)       #具体请求处理
        connfd.close()


if __name__=="__main__":
    main()