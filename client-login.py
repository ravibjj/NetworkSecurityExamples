#!/usr/bin/env python3

import socket

s = socket.socket()
s.connect(("127.0.0.1", 1337))
welcome_message = s.recv(2048).decode()
print(welcome_message)
username = input("")
s.send(username.encode())
ans = s.recv(1024).decode()
print(ans)
password = input("")
s.send(password.encode())
ans = s.recv(2048).decode()
print(ans)
s.close()