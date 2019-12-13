from pwn import *

host = '127.0.0.1'
port = 1337

connection = remote(host, port)

prompt = connection.recv()

print(prompt)

connection.close()
