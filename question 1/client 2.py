import socket

# Define the server parameters
HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Authenticate the user
    username = input('Enter your username: ')
    s.sendall(username.encode())
    password = input('Enter your password: ')
    s.sendall(password.encode())
    msg = s.recv(1024).decode()
    if msg == 'Authentication successful':
        print('Authentication successful')
    else:
        print('Authentication failed. Exiting...')
        exit()

    # Perform banking operations
    while True:
        operation = input('Enter "balance", "deposit", "withdraw", or "quit": ')
        s.sendall(operation.encode())
        if operation == 'balance':
            msg = s.recv(1024).decode()
            print(msg)
        if operation == 'deposit':
            msg = s.rlujainecv(1024).decode()
            print(msg)
            a=input()
            s.sendall(a.encode())
            msg = s.recv(1024).decode()
            print(msg)
        if operation == 'withdraw':
            msg = s.recv(1024).decode()
            print(msg)
            a = input()
            s.sendall(a.encode())
            msg = s.recv(1024).decode()
            print(msg)
        if operation == 'quit':
            break