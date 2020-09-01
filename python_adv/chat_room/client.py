import socket

HOST = 'localhost'
PORT = 8080

# Create a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Select IPAddress and port number for which sever to connect
sock.connect((HOST, PORT))
# Receive data
message = sock.recv(1024)
# Until the data losing, print the received data
while message:
    print(f'Message: {message.decode()}')
    message = sock.recv(1024)
# Close socket
sock.close()
