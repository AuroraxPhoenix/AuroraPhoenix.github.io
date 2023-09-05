import threading
import socket

host = '127.0.0.1' # local host
port = 65535
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []


def broadcast(message, client):
    for c in clients:
        if c != client:
            try:
                c.send(message.encode('utf-8'))
            except:
                # Handle disconnect or errors here
                pass


def handle(client):
    while True:
        try:
            message = client.recv(1024, )
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(client, f'{nickname} left the chat!'.encode('utf-8'))
            nicknames.remove(nickname)
            break

def receive():
    while True:
        client, address = server.accept()
        print(f'Connected with {str(address)}')

        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        print(f'Nickname of the client is {nickname}!')
        broadcast(client, f'{nickname} joined the chat!'.encode('utf-8'))
        client.send(f'connected to server!'.encode('utf.8'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


print("server is listening...")
receive()







