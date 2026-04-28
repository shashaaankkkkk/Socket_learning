import socket
import threading

SERVER_IP = "192.168.31.70"   #  "192.168.31.70"
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, PORT))

nickname = input("Enter your nickname: ")


def receive():
    while True:
        try:
            message = client.recv(1024).decode("utf-8")

            if message == "NICK":
                client.send(nickname.encode("utf-8"))
            else:
                print(message)

        except:
            print("Connection closed")
            client.close()
            break


def send():
    while True:
        msg = input("")
        message = f"{nickname}: {msg}"

        try:
            client.send(message.encode("utf-8"))
        except:
            break

        if msg == "quit":
            client.close()
            break


# Run both threads
threading.Thread(target=receive).start()
threading.Thread(target=send).start()
