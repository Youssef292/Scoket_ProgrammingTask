# SENDER

import socket

ip = "127.0.0.1"
port = 5001
msg = b"hello Receiver"

print(f'Sending {msg} to {ip}:{port}')

sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)
sock.sendto(msg, (ip, port))