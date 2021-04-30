import socket
import sys
import threading

# function send_message() to send message to the server
def send_message(clientSock):
    # input client's username as identity
    username = input("Input username: ")

    # input message and send it to the server
    while True:
        message = input()
        message_send = username + ': ' + message
        clientSock.sendto(message_send.encode("utf-8"), ("", UDP_PORT_NO))

        # to delete message input
        sys.stdout.write("\033[F")

# declare ip address and port
UDP_IP_ADDRESS = '0.0.0.0'
UDP_PORT_NO = 2410

# create socket
clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# allows sockets to bind() to the same IP:port 
clientSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

# allows broadcast UDP packets to be sent and received
clientSock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# bind the socket to address
clientSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))

# print additional message
print("\nWelcome to WhatsUp Messenger!")

# create object Thread
clientThread = threading.Thread(target=send_message, args=(clientSock,))
clientThread.start()

# receive broadcast message from server and print it
while True:
    data, addr = clientSock.recvfrom(1024)
    print(data.decode("utf-8"))