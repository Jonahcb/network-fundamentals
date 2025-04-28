from socket import *

serverName = 'hostname' # Replace with the server's IP address or hostname
serverPort = 12000 # Replace with server's port number

clientSocket = socket(AF_INET, SOCK_DGRAM) # Establish client's socket using port assigned by OS

message = input("Input lowercase sentence: ") # Prompt the user for a message
clientSocket.sendto(message.encode(), (serverName, serverPort)) # Send the message to the server

modifiedMessage, serverAddress = clientSocket.recvfrom(2048) # Receive a response from the server
print(modifiedMessage.decode()) # Print the response
clientSocket.close() # Close the socket
