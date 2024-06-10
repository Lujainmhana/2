import socket
import threading

# Define the server parameters
HOST = '127.0.0.1'
PORT = 65432

# Define the account details
accounts = {
    'lama': {'password': '2795', 'balance': 1000.0},
    'danial': {'password': '2836', 'balance': 500.0},
    'lujain': {'password': '2894', 'balance': 2000.0}
}

# Function to handle a client connection
def handle_client(conn, addr):
    print(f'New connection from {addr}')

    # Authenticate the client
    while True:
        username = conn.recv(1024).decode()
        password = conn.recv(1024).decode()
        if username in accounts and accounts[username]['password'] == password:
            conn.sendall(b'Authentication successful')
            break
        else:
            conn.sendall(b'Invalid username or password. Please try again.')

    # Handle banking operations
    while True:
        operation = conn.recv(1024).decode().strip()
        if operation == 'balance':
            balance = accounts[username]['balance']
            conn.sendall(f'Your current balance is: {balance:.2f}'.encode())
        elif operation == 'deposit':
            conn.sendall(b'Enter the amount to deposit:')
            amount = float(conn.recv(1024).decode().strip())
            accounts[username]['balance'] += amount
            conn.sendall(f'Deposit successful. Your new balance is: {accounts[username]["balance"]:.2f}'.encode())
        elif operation == 'withdraw':
            conn.sendall(b'Enter the amount to withdraw:')
            amount = float(conn.recv(1024).decode().strip())
            if amount <= accounts[username]['balance']:
                accounts[username]['balance'] -= amount
                conn.sendall(f'Withdrawal successful. Your new balance is: {accounts[username]["balance"]:.2f}'.encode())
            else:
                conn.sendall(b'Insufficient funds.')
        elif operation == 'quit':
            conn.sendall(f'Your final balance is: {accounts[username]["balance"]:.2f}'.encode())
            break
        else:
            conn.sendall(b'Invalid operation. Please try again.')

    print(f'Closing connection with {addr}')
    conn.close()

# Start the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f'Server listening on {HOST}:{PORT}')

    while True:
        conn, addr = s.accept()
        threading.Thread(target=handle_client, args=(conn, addr)).start()