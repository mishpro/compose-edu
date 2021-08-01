import socket
from recvall import recv_msg, send_msg
import os
import subprocess as sp
import time

from checkdirs import checknmake, mkfiles

address = ('localhost', 8787)
script_dir = os.path.dirname(os.path.abspath(__file__))

shared = checknmake(script_dir)
# complete = sp.run('docker run --name=exp-logs -dp 8787:8787 -v '+shared+':/_shared exp/server-2', shell=True)
sp.run('docker-compose up -d', shell=True)
mkfiles(shared, 'file_')


with socket.create_connection(address) as sock:
    send_msg(sock, 'test str test str test str 1234567890ABCDEF/,..'.encode())
    data1 = recv_msg(sock).decode()
    data2 = recv_msg(sock).decode()
    print(data1, data2)

print('_____________')
print('[compose] Logs from container')
sp.run('docker-compose logs', shell=True)
print('_____________')
# sp.run('docker-compose down', shell=True)
# sp.run('docker rm exp-logs',shell=True)
