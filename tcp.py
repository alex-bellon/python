import socket

s = socket.socket()
host = 'stack.overflow.fail'
port = 7000

s.connect((host, port))

recv = s.recv(1024).decode('ascii')
print(recv)

resp = 'Sample response'
s.send(resp.encode('ascii'))

s.close()
