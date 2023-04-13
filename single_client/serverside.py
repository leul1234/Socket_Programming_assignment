import random
from socket import *

serverPort = 65432
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('server is ready to receive')
serverName= "leul_yitayew"

randomNumber = random.randint(1,100)
while True:

    connectionSocket, addr = serverSocket.accept()

    sentence = connectionSocket.recv(1024).decode().split(',')

    recievedNum = int(sentence[1])
    

    clientName=sentence[0]

    summation = recievedNum + randomNumber
    
    print(f'the server: {serverName}')
    print(f'client name: {clientName}')
    print(f'client number: {recievedNum}')
    print(f'server generated number: {randomNumber}')
    print(f'total sum: {summation}')
    print("===================================")
    connectionSocket.sendto(f'the server name is: {serverName},the client name is : {clientName},the client input number is: {recievedNum},server generated number is: {randomNumber},total sum is: {summation}'.encode(),addr)

    if recievedNum>100 or recievedNum<1:
        print("server is terminated")
        serverSocket.close()
        break

    
serverSocket.close()