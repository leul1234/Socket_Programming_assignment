
from socket import *
serverName = 'localhost'
serverPort = 65432
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

keyboardInput = input('Input an intiger number from 1 to 100 : ')
sentence = 'Leulseged,'
if len(keyboardInput)!=0:
    clientSocket.send(sentence.encode()+ keyboardInput.encode())
    modifiedSentence = clientSocket.recv(1024)
    information = modifiedSentence.decode().split(',')
    for i in information:
            print(i)
else:
    print('connection terminated becuase you send nothing or your server become shutdown !')
    clientSocket.close()
clientSocket.close()