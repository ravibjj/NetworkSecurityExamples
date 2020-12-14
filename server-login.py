#!/usr/bin/env python3
import socket

s = socket.socket()
s.bind(("0.0.0.0", 1337))
s.listen(1)
conn, addr = s.accept()
conn.send("Welcome to the server!\nUsername".encode())
username = conn.recv(4096).decode()
conn.send("Password: ".encode())
password = conn.recv(4096).decode()
if username == "John" and password == "Pa$$w0rd":
    conn.send("Hello {}, Have a great day!".format(username).encode())
else:
    conn.send("Wrong details, Please try again later".encode())
s.close()