from socket import *
import codecs

serverName = "127.0.0.1"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
file = input('Input filename:')
store = input('Input store location:')
clientSocket.send(file.encode())
receiveCode = clientSocket.recv(1024)
print('From Server:', receiveCode.decode())
if receiveCode.decode() == "200 ok":
    receiveFile = ''
    while 1:
        packet = clientSocket.recv(1024).decode()
        breaking = False
        for i in range(len(packet) - 1):
            if packet[i] == '\t' and packet[i+1] == '\n':
                breaking = True
                break
        receiveFile += packet
        if breaking:
            break
    f = codecs.open(store + ".html", "w", "utf-8")
    f.write(receiveFile)
clientSocket.close()
