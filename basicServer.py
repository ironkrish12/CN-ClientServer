import socket

s = socket.socket()
print("Socket created!")

s.bind(('localhost',9999))#localhost is IP, 9999 is port number,we bind socket with port number

s.listen(5)#3 clients
print("Waiting for connection")
while True:
    c, addr= s.accept()#If we want the server,gives client socket 'c' and address
    print("Connected with ",addr)
    s.send(bytes('welcome to Telusko','utf-8'))