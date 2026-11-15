print("Server Start")
from socket import *
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('localhost', 8080))
server_socket.listen(10)
print("Server чекає на клієнтів")

clients = []
server_socket.setblocking(False)

while True:

    try:
        connect, address = server_socket.accept()
        print("Клієнт підключився",address)
        connect.send("Привіт новий супер користувач". encode())
        client_name = connect.recv(1024).decode()
        print("НОВИЙ КОРИСТУВАЧ", client_name)
        connect.setblocking(False)
        clients.append(connect, client_name)


    except:
        pass
    for client in clients:
        try:
            messange = client[0].recv(1024).decode().strip()
            print(f"{client[1]}: {messange}")
            for c in clients:
                if client != c:
                    c[0].send(f'{client[1]}: {messange}'.encode())

        except BlockingIOError:
            pass

        except:
            print(f'Клієнт {client[1]} відключився.')
            client[0].close()
            clients.remove(client)