import socket
import threading

nickname = input("Choose an nickname: ")
host = '127.0.0.1'
port = 65535
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')

            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("An error orrurred!")
            client.close()
            break

def write():
    while True:
        message = f'{nickname} : {input("")}'
        if message == 'exit':
            client.close()
        else:
            client.send(message.encode('utf-8'))


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()



