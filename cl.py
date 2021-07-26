import socket
from recvall import recv_msg, send_msg
import os
import subprocess as sp
import time

address = ('localhost', 8787)
# sock = socket.socket()
complete = sp.run('docker run --name=exp-logs -dp 8787:8787 exp/server-1', shell=True)
# print(complete.returncode)
# time.sleep(2)

with socket.create_connection(address) as sock:
    send_msg(sock, 'test str test str test str 1234567890ABCDEF/,..'.encode())
    data = recv_msg(sock).decode()
    print(data)
    # try:
        # data = recv_msg(sock).decode()
        # print(data)
    # except ConnectionRefusedError:
        # sock.connect(address)
        # print('OK 2nd try')
print('_____________')
sp.run('docker logs exp-logs', shell=True)
print('_____________')
sp.run('docker stop exp-logs', shell=True)
sp.run('docker rm exp-logs',shell=True)
