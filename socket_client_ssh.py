import socket,os

client = socket.socket()
# client.connect(("39.106.156.185",9999))
client.connect(("loaclhost",9999))
while True:
    msg = input(">> ").strip()
    if not msg:
        continue
    elif not os.path.isfile(msg):
        print("file don't exsist")
        continue
    client.send(msg.encode())
    f = open(msg,'rb')
    data = f.read()
    f.close()
    client.send(str(len(data)).encode())
    ack = client.recv(1024)
    client.send(data)   #encode（）用某种方式编码
    # client.send(msg.decode())    #str不能直接发送,且字符串不能被解码。
    # count = 0
    # size = int(client.recv(1024).decode())
    # # client.send(b"Y")
    # while count < size:
    #     data = client.recv(1024)     #当接收的数据大于1024时无法完全接收。
    #     count += len(data.decode())            # 但是调整数值又不能准确地知道要收多少。
    #                                 #所以，可以让服务端先发送信息的大小，
    #                                 # 客户端再准备对应大小的缓冲区
    #     print(data.decode())
    #     print("total size",count)   #因为有中文的原因，所以count会大于size。
    #                            # 解决在客户器端，应该先编码在判断长度
    #     print("size",size)
client.close()