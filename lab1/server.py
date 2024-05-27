import socket
import os

if not os.path.isdir("server_files"):
    os.makedirs('server_files')


def receive_file(connection: socket, filename: str):
    print("receive file")

    print(f'{filename=}')
    with open("server_files/" + filename, "wb") as file:
        iteration = 0
        while response := connection.recv(1024):
            iteration += 1
            print(f'{iteration=} of file receiving')
            file.write(response)

    print("File saved")


def send_file(connection: socket, filename: str):
    print("send file")
    print(f"{filename=}")

    with open("server_files/" + filename, 'rb') as file:
        while data := file.read(1024):
            connection.sendall(data)
    print(f'File {filename} sent successfully')


if __name__ == "__main__":
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.bind(("", 9090))
    socket.listen()

    while True:
        connection, address = socket.accept()
        with connection:
            print("Connected: ", address)
            command, filename = connection.recv(256).decode().split(",")
            connection.send(b"accepted")
            print(f'{command=}')
            if command == 'send':
                receive_file(connection, filename)
            elif command == 'request':
                send_file(connection, filename)
