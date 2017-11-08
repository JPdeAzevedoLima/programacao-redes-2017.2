#!/usr/bin/python3.6

import socket
import threading

class ThreadedServer(object):
    #Construtor
    def __init__(self,host,port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #Permitir o reuso da porta encerrada
        self.sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.sock.bind((self.host,self.port))

    def listen(self):
        self.sock.listen(5)
        while True:
            client,address = self.sock.accept()
            #Timeout do cliente
            client.settimeout(60)
            print("Conexão de: ",address)
            threading.Thread(target = self.listenToClient,args = (client,address)).start()

    def listenToClient(self,client,address):
        size = 1024
        while True:
            #Tratamento de exceção
            try:
                data = client.recv(size)
                print("\nMensagem recebida: ",repr(data))
                #Se receber dados, enviará de volta como um eco, a mesma mensagem
                if data:
                    response = data
                    client.send(response)
                else:
                    raise error('Cliente desconectado!')
            #Bloco de código que deve ser executado mesmo no caso de erro
            except:
                client.close()
                return False

if __name__ == "__main__":
    while True:
        port_num = input("Porta: ")
        try:
            port_num = int(port_num)
            break
        except ValueError:
            pass

    ThreadedServer('127.0.0.1',port_num).listen()
