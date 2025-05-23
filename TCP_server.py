import socket

serverPort = 12000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print('The server is ready to receive')

while True:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024)
    print(sentence.decode())  
    if sentence.decode() != 'exit':
        capitalizedSentence = sentence.decode().upper() 
        connectionSocket.send(capitalizedSentence.encode()) 
    else: 
        connectionSocket.close()
