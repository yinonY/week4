import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest_ip = '127.0.0.1'
dest_port = 12345
s.connect((dest_ip, dest_port))

msg = input("Enter text ('exit' to close): ")
while not msg == 'exit':
    s.send(bytes(msg, 'utf-8'))
    data = s.recv(4096)
    print("Server sent: ", data.decode('utf-8'))
    msg = input("Enter text ('exit' to close): ")

s.close()