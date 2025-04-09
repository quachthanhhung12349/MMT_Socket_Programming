from socket import *
import sys
import threading
serverPort = 12000

def handleClient(connectionSocket):
    addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024)
    print(sentence.decode())  
    if sentence.decode() != 'exit':
        capitalizedSentence = sentence.decode().upper() 
        connectionSocket.send(capitalizedSentence.encode()) 
    else: 
        connectionSocket.close()


def main():
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    serverSocket.listen(5)
    print(f"Server listening on port {serverPort}...")
    try:
        while True:
            # Accept a connection from a client
            connectionSocket, addr = serverSocket.accept()
            print(f"Accepted connection from {addr}")
            
            # Start a new thread to handle the client
            client_thread = threading.Thread(
                target=handleClient, 
                args=(connectionSocket,)
            )
            client_thread.start()
    except KeyboardInterrupt:
        print("\nShutting down server...")
        serverSocket.close()
        sys.exit()


    

if __name__ == "__main__":
    main()



