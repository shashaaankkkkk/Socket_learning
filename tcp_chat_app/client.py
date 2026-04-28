import socket 
dest_ip="127.0.0.1"
dest_port=12345
client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((dest_ip,dest_port))
while True:
    message=client_socket.recv(1024).decode("utf-8")
    if message=="quit":
        client_socket.send("quit".encode("utf-8"))
        print("connecttion bye bye")
        break
    else:
        print(f"Dusri side : {message}\n")
        message=input("Lodu_anshul:")
        client_socket.send(message.encode("utf-8"))
client_socket.close()
