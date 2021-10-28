import codecs
from socket import *

serverPort = 12000
server = 'localhost'
message1 = "200 ok"
message2 = "404 Not Found"
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((server, serverPort))
serverSocket.listen(1)
print('The server is ready to receive')

while True:
    connectionSocket, addr = serverSocket.accept()
    fileName = connectionSocket.recv(1024).decode()
    try:
        file = codecs.open("ServerFile/" + fileName, 'r', "utf-8")
        content = file.read() + '\t\n'
        connectionSocket.send(message1.encode())
        connectionSocket.send(content.encode())

    except FileNotFoundError:
        connectionSocket.send(message2.encode())

    connectionSocket.close()
