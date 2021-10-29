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
    packet = []
    unCompletePreviousChars = []
    while 1:
        try:
            packet = clientSocket.recv(1024)
            for i in range(len(packet)):
                unCompletePreviousChars.append(packet[i])
            packet = bytes(unCompletePreviousChars)
            unCompletePreviousChars = []
            packet = packet.decode()
        except UnicodeDecodeError:
            lastIndex = len(packet) - 1
            newPacket = list(packet)
            for i in range(lastIndex, 0, -1):
                newPacket.pop()
                unCompletePreviousChars.append(packet[i])
                if str(bin(packet[i]))[3] != '0':
                    break
            packet = bytes(newPacket)
            packet = packet.decode()
        breaking = False
        for i in range(len(packet) - 1):
            if packet[i] == '\t' and packet[i + 1] == '\n':
                breaking = True
                break
        receiveFile += packet
        if breaking:
            break
    f = codecs.open(store + ".html", "w", "utf-8")
    f.write(receiveFile)
clientSocket.close()
