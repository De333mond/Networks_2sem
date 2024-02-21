import os
import socket


def request_file(filename: str):
    s = socket.socket()
    s.connect(("localhost", 9090))

    s.send(b'request,' + filename.encode())
    accepted = s.recv(128)

    with open('client_files/' + filename, "wb") as file:
        while response := s.recv(1024):
            file.write(response)
    print("file accepted")
    s.close()


def send_file(filename: str):
    s = socket.socket()
    s.connect(("localhost", 9090))

    s.send(b"send," + filename.encode())
    accepted = s.recv(1024)
    with open(filename, 'rb') as file:
        while data := file.read(1024):
            s.sendall(data)
    print(f'File {filename} sent successfully')
    s.close()


if __name__ == "__main__":
    is_running = True

    while is_running:
        command = input('Enter command (send, request): ')
        if command == '':
            is_running = False

        filename = input('Enter filename: ')
        if not os.path.exists(filename):
            print('This file is not exists!')
            continue

        if command == 'send':
            send_file(filename)
        elif command == 'request':
            request_file(filename)
