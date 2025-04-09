from socket import *
import threading
import sys

serverPort = 6789

def handle_client(connectionSocket):
    try:
        # Receive and decode the client request
        message = connectionSocket.recv(1024).decode()
        # Hardcode the filename to serve
        filename = "HelloWorld.html"
        
        # Read the file and prepare the HTTP response
        with open(filename, 'r') as f:
            outputdata = f.read()
        response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n" + outputdata
        connectionSocket.sendall(response.encode())
    
    except IOError:
        # Handle file not found
        error_response = "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n<h1>404 Not Found</h1>"
        connectionSocket.sendall(error_response.encode())
    
    finally:
        # Close the connection
        connectionSocket.close()

def main():
    # Create the server socket
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    serverSocket.listen(5)  # Allow up to 5 pending connections
    print(f"Server listening on port {serverPort}...")

    try:
        while True:
            # Accept a connection from a client
            connectionSocket, addr = serverSocket.accept()
            print(f"Accepted connection from {addr}")
            
            # Start a new thread to handle the client
            client_thread = threading.Thread(
                target=handle_client, 
                args=(connectionSocket,)
            )
            client_thread.start()
    
    except KeyboardInterrupt:
        print("\nShutting down server...")
        serverSocket.close()
        sys.exit()

if __name__ == "__main__":
    main()