import socket,os

server = socket.socket()
server.bind(("localhost",9998))
server.listen()
print("listen start")
while True:
    print("new connct")
    con,addr = server.accept()
    while True:
        print("wait")
        data = con.recv(1024).decode()   #decode（）解码
        print("data:",data)
        # data = con.recv(1024)      #注意收到的字符串时byte，不能用os模块执行必须要解码
        if not data:
            print("lose connect")
            break
        print("end")
        msg = os.popen(data).read() #当msg为空时，程序会出现错误
        # print(data)
        if len(msg)==0:       #因为msg为空所以必须赋值。
                             # 如果continue，data就收不到东西。
                             # 如果break，就断开了当前连接
            msg = "error "
        print(len(msg))
        con.send(str(len(msg)).encode())  #注意在linux中可能会出现socket 粘包
                                 # socket 粘包。就是两个send的内容合在一起了
        ack = con.recv(1024)#粘包解决办法，可以在两次send之间加入一次交互如recv。再握一次手表示确认
        con.send(msg.encode())
        # print("end")

con.close()
