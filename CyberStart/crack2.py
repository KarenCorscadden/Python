import socket

HOST = 'services.cyberprotection.agency'  # The server's hostname or IP address
PORT = 13777        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    #s.sendall(b'Hello, world')
    data1 = s.recv(2048)

print('Received', repr(data1))

with open("chal3", "wb") as file:
  file.write(data1)


