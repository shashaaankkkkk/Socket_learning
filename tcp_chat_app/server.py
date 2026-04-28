import socket
hostname=socket.gethostbyname(socket.gethostname())
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(("192.168.31.70",12345))
server_socket.listen()
client_socket,address=server_socket.accept()
client_socket.send("you r connected".encode("utf-8"))
while True:
    message=client_socket.recv(1024).decode("utf-8")
    if message=="quit":
        client_socket.send("quit".encode("utf-8"))
        print("ending connection and chat")
        break
    else:
        print(f'Lodu_anshul :{message}\n')
        message=input("You : ")
        client_socket.send(message.encode("utf-8"))

server_socket.close()
