import random
import threading
from socket import *

socket2 = socket(AF_INET, SOCK_DGRAM)
socket2.connect(('8.8.8.8',80))
ipAddress = socket2.getsockname()[0]

def multithread(connectionSocket, addr):
    sentence = connectionSocket.recv(1024).decode().split(',')
    recievedNum = int(sentence[1])

    clientName = sentence[0]

    summation = recievedNum + randomNumber

    print(f'the server: {serverName}')
    print(f'client name: {clientName}')
    print(f'client number: {recievedNum}')
    print(f'server generated number: {randomNumber}')
    print(f'total sum: {summation}')
    print("===================================")
    connectionSocket.sendto(
        f'the server name is: {serverName},the client name is : {clientName},the client input number is: {recievedNum},server generated number is: {randomNumber},total sum is: {summation}'.encode(),
        addr)

    if recievedNum > 100 or recievedNum < 1:
        print("server is terminated")
        serverSocket.close()


serverPort = 65432
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(2)

print('server is ready to receive')
print(f'any one can connect with this server using port number {serverPort} and ip address {ipAddress}')
serverName = "leul_yitayew"

while True:
    randomNumber = random.randint(1, 100)
    connectionSocket, addr = serverSocket.accept()

    user = threading.Thread(target=multithread, args=(connectionSocket, addr))
    user.start()

serverSocket.close()