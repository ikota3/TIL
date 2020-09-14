import socket
from threading import Thread

HOST = 'localhost'
PORT = 8080
CLIENTS = {}
ADDRESSES = {}

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))


def accept_client_connection() -> None:
    while True:
        client_conn, client_address = sock.accept()
        ADDRESSES[client_conn] = client_address
        print(f'{client_address} has connected')
        msg = 'Welcome to the chat room, Please type your name to continue.'
        client_conn.send(msg.encode('utf8'))

        Thread(
            target=handle_clients,
            args=(
                client_conn,
                client_address)
        ).start()


def handle_clients(conn, address) -> None:
    name = conn.recv(1024).decode('utf8')
    msg = f'Welcome {name}. You can type #quit if you ever want to leave the chat room.'
    conn.send(msg.encode('utf8'))
    msg = f'{name} has recently joined the chat room.'
    broadcast(msg)
    CLIENTS[conn] = name

    while True:
        msg = conn.recv(1024).decode('utf8')
        if msg != "#quit":
            broadcast(msg, f'{name}: ')
        else:
            conn.send("#quit".encode('utf8'))
            conn.close()
            del CLIENTS[conn]
            broadcast(f'{name} has left the chat room.')
            break


def broadcast(msg: str, prefix: str = "") -> None:
    for client in CLIENTS:
        client.send(f'{prefix}{msg}'.encode("utf8"))


if __name__ == '__main__':
    sock.listen(5)
    print("The server is listening...")

    client_conn_thread = Thread(target=accept_client_connection)
    client_conn_thread.start()
    client_conn_thread.join()
