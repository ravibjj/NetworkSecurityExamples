#!/bin/bash
# ****** Ravi Nori
# ****** 12/11/2020
# ****** Purpose: create a client socket
import socket
import time

# connect to the listener
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 1424))
time.sleep(30)
# test host/port
print("you are connecting to {}:{}".format(host, port))
s.close()
