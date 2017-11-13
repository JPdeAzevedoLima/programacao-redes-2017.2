#!/usr/bin/python3.6

import socket

serverHost = 'localhost'
serverPort = 12000

clientSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

message = input("Entre com a string minuscula: ")
byte_msg = message.encode('utf-8')

clientSocket.sendto(byte_msg,(serverHost,serverPort))
modifiedMessage,serverAddress = clientSocket.recvfrom(1024)
print(modifiedMessage)
print(modifiedMessage.decode('utf-8'))
clientSocket.close()
