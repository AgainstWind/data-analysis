import socket
import sys

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999
server.bind((host,port))
server.listen(5) #max connection

while True:
    client,addr = server.accept()
    print("client address: %s"%str(addr))
    msg = 'hello from server'
    client.send(msg.encode('utf-8'))
    client.close()