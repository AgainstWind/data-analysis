import socket
import sys

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999
client.connect((host,port))

msg = client.recv(1024) #receive bytes less than 1024
client.close()
print(msg.decode('utf-8'))

