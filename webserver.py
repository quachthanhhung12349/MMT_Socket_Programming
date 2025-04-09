#import socket module
from socket import *
import sys # In order to terminate the program
serverPort = 6789
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    print('Received a connection from:', addr)
    try:
        message = connectionSocket.recv(1024).decode()
        filename = "HelloWorld.html"
        f = open(filename) #file name is in the second part of the message
        
        outputdata = f.read()
        f.close()
        #Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/html\r\n".encode())
        print("Sending the file content...")

        #Send the content of the requested file to the client
        connectionSocket.sendall(outputdata.encode())
        connectionSocket.send("\r\n".encode())
        print("File sent successfully.")

        # Close the client connection
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        print("File not found")
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n".encode())
        connectionSocket.send("Content-Type: text/html\r\n".encode())

        # Close the client connection
        connectionSocket.close()
    serverSocket.close()
    sys.exit()#Terminate the program after sending the corresponding data