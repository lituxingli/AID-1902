# from socket import *
#
# # 创建tcp套接字
# s = socket()
# #setsockopt   设置套接字选项
# s.setsockopt(SOL_SOCKET,SO_REUSEADDR,True)
# s.bind(('0.0.0.0',8000))
# s.listen(5)
#
# c,addr = s.accept()
# print("Connect from",addr)
# data = c.recv(4096)
# print(data)
#
# data="""HTTP/1.1 200 OK
# Content-Type: text/html
#
# Hello world
# """
#
# c.send(data.encode())
#
# c.close()
# s.close()




from socket import *
sockfd=socket()
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,True)
sockfd.bind(('0.0.0.0',9000))
sockfd.listen(3)

print('waitting')
connfd,addr=sockfd.accept()
print("connect from:",addr)

data=connfd.recv(1024)
print(data)

data="""HTTP/1.1 200 OK
Content-Type: text/html

Hello world  chvdagvd
"""
connfd.send(data.encode())


connfd.close()
sockfd.close()