# Python_Adv

## Socket Connection

`socket`を使うことによって，ソケット通信を行うことができる．

- `server.py`

  ```py
  import socket

  HOST = 'localhost'
  PORT = 8080
  # IF_INET=IPV4，SOCK_STREAM=TCP
  _socket = socket.socket(socket.IF_INET, socket.SOCK_STREAM)
  _socket.bind((HOST, PORT))
  # Listen for 1 connection
  _socket.listen(1)
  # Get connection and address
  conn, address = _socket.accept()
  # Send data
  conn.send("Hello!")
  # Close connection
  conn.close()
  ```

- `client.py`

  ```py
  import socket

  HOST = 'localhost'
  PORT = 8080

  _socket = socket.socket(socket.IF_INET, socket.SOCK_STREAM)
  # Select which server to connect to
  _socket.connect((HOST, PORT))
  # Receive data(1024byte)
  message = _socket.recv(1024)
  while message:
    print(f'Message: {message}')
    message = _socket.recv(1024)
  # Close socket
  _socket.close()
  ```
