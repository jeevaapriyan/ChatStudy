import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 12345  ))
print("Connected to server")

while True:
    message = input("Client: ")
    client_socket.send(message.encode())

    if message.lower() == "exit":
        break
    reply = client_socket.recv(1024).decode()
    print("Server:", reply)
client_socket.close()