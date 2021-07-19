import socket
from recvall import recv_msg, send_msg
import os
import subprocess as sp
import time

address = ('localhost', 8787)
sock = socket.socket()
complete = sp.run('docker run --rm -dp 8787:8787 exp/server', stdout=True, shell=True)
print(complete.returncode)
# time.sleep(2)

sock.connect(address)
send_msg(sock, 'test str'.encode())

data = recv_msg(sock).decode()
print(data)

print('------')
print(complete.stderr)
