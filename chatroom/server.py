import socket
import threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind(("0.0.0.0", 12345))
server_socket.listen()

clients = []
nicknames = []


def broadcast(message):
    for client in clients:
        try:
            client.send(message.encode("utf-8"))
        except:
            pass


def handle_client(client):
    while True:
        try:
            message = client.recv(1024).decode("utf-8")
            if not message:
                break
            broadcast(message)
        except:
            index = clients.index(client)
            nickname = nicknames[index]

            print(f"{nickname} disconnected")

            clients.remove(client)
            nicknames.remove(nickname)
            client.close()

            broadcast(f"{nickname} left the chat")
            break


def accept_clients():
    while True:
        client, address = server_socket.accept()
        print(f"Connected with {address}")

        client.send("NICK".encode("utf-8"))
        nickname = client.recv(1024).decode("utf-8")

        clients.append(client)
        nicknames.append(nickname)

        print(f"Nickname: {nickname}")

        broadcast(f"{nickname} joined the chat")
        client.send("Connected to server".encode("utf-8"))

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()


print("Server running...")
accept_clients()
