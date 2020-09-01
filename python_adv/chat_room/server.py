import socket

HOST = 'localhost'
PORT = 8080

# Create a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind IPAddress and port number
sock.bind((HOST, PORT))
# Listen for 1 connection
sock.listen(1)
# When client connected, get the connection and the address
conn, address = sock.accept()
# Using connection for sending data
message = f'Sending message from sever to {address}...'
conn.send(message.encode())
# Close connection
conn.close()
