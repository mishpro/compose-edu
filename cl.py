import socket
from recvall import recv_msg, send_msg
import os
import subprocess as sp
import time

address = ('localhost', 8787)
sock = socket.socket()
complete = sp.run('docker run --name=exp-logs -dp 8787:8787 exp/server', shell=True)
# print(complete.returncode)
# time.sleep(2)

sock.connect(address)
    
send_msg(sock, 'test str'.encode())

data = recv_msg(sock).decode()
print(data)
print('_____________')
sp.run('docker logs exp-logs', shell=True)
print('_____________')
sp.run('docker rm exp-logs',shell=True)
