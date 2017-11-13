#!/usr/bin/python3.6

import socket

serverHost = 'localhost'
serverPort = 12000

serverSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

serverSocket.bind((serverHost,serverPort))

print("Servidor pronto para receber:\n")

while True:
    message,clientAddress = serverSocket.recvfrom(1024)
    print('Conexão de: ', clientAddress)
    #Processar a string para letras maiusculas
    modifiedMessage = message.upper()
    print("\n",modifiedMessage)
    #Enviar mensagem em maiusculas
    serverSocket.sendto(modifiedMessage,clientAddress)
