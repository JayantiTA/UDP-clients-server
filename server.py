import socket
import sys
import threading

# define ip address and port
UDP_IP_ADDRESS = '127.0.0.1'
UDP_PORT_NO = 2410

# create a socket
serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# bind the socket to address
serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))

# allows sockets to bind() to the same IP address and port 
serverSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
serverSock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

print("\n!!!Server is ready!!!")
print("\nYour chats will be recorded here")

# handle message receiving 
while True:
    # receive message from clients
    message, address = serverSock.recvfrom(1024)
    message_send = message.decode("utf-8")
    # print message
    print(message_send)
    # send broadcast message to all clients
    serverSock.sendto(message_send.encode("utf-8"), ('<broadcast>', UDP_PORT_NO))