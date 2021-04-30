# UDP-clients-server
This project was created to fulfill Ichiro's third internship assignment - **Group Chat** using clients-server (UDP implementation)

# UDP Implementation - Group Chat
## General Explanation
What is UDP?

    UDP or User Datagram Protocol is connection-less protocol which is suitable for applications that require efficient communication that doesn't have to worry about packet loss. 

How does UDP work?

    It sends packets (units of data transmission) directly to a target computer, without establishing a connection first, indicating the order of said packets, or checking whether they arrived as intended (UDP packets are referred to as ‘datagrams’).

This program, **Group Chat**, uses UDP for data transfer between clients and server. Some clients (more than 1) can send message to others and receive messgae from others. This program also uses **broadcast** message which is sent from server to all clients. The program also uses **threading**, so it can input message and send message to server simultaneously.

## Documentation
### Server Code
Use library `socket`, `sys`, and `threading`
```py
import socket
import sys
import threading
```

Declare ip address and port
```py
UDP_IP_ADDRESS = '127.0.0.1'
UDP_PORT_NO = 2410
```

Create a socket
```py
serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
```

Bind the socket to address
```py
serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))
```

Allows sockets to bind() to the same IP:port
```py
serverSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
serverSock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
```

Print additional message
```py
print("\n!!!Server is ready!!!")
print("\nYour chats will be recorded here")
```

Handle message receiving 
```py
while True:
    # receive message from clients
    message, address = serverSock.recvfrom(1024)
    message_send = message.decode("utf-8")
    # print message
    print(message_send)
    # send broadcast message to all clients
    serverSock.sendto(message_send.encode("utf-8"), ('<broadcast>', UDP_PORT_NO))
```

### Clients Code
Use library `socket`, `sys`, and `threading`
```py
import socket
import sys
import threading
```

Function send_message() to send message to the server
```py
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
```

Declare ip address and port
```py
UDP_IP_ADDRESS = '0.0.0.0'
UDP_PORT_NO = 2410
```

Create socket
```py
clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
```

Allows sockets to bind() to the same IP:port 
```py
clientSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
```

Allows broadcast UDP packets to be sent and received
```py
clientSock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
```

Bind the socket to address
```py
clientSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))
```

Print additional message
```py
print("\nWelcome to WhatsUp Messenger!")
```

Create object Thread
```py
clientThread = threading.Thread(target=send_message, args=(clientSock,))
clientThread.start()
```

Receive broadcast message from server and print it
```py
while True:
    data, addr = clientSock.recvfrom(1024)
    print(data.decode("utf-8"))
```

## References
https://docs.python.org/3/library/socket.html

https://erlerobotics.gitbooks.io/erle-robotics-python-gitbook-free/content/udp_and_tcp/socket_options.html

https://tech.flipkart.com/linux-tcp-so-reuseport-usage-and-implementation-6bfbf642885a

https://www.cloudflare.com/learning/ddos/glossary/user-datagram-protocol-udp/