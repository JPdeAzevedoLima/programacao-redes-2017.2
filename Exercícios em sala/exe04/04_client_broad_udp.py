#!/usr/bin/python3.6

import socket

serverHost = '10.25.255.255'
serverPort = 12000

clientSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
clientSocket.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST, 1)

message = input("Entre com a string minuscula: ")
byte_msg = message.encode('utf-8')

clientSocket.sendto(byte_msg,(serverHost,serverPort))
modifiedMessage,serverAddress = clientSocket.recvfrom(1024)
print(modifiedMessage)
print(modifiedMessage.decode('utf-8'))
clientSocket.close()
