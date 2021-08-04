import socket
from struct import error
import time

from docker import client
from recvall import recv_msg, send_msg
import os

from checkdirs import checknmake, mkfiles

import docker

addr = ('localhost', 8787)
script_dir = os.path.dirname(os.path.abspath(__file__))

shared = checknmake(script_dir)
'''
Особенность параметра ports функции run в том, что сначала специфицируется порт в контейнере, а затем порт хоста 
Т.е. в отличие от команды docker run -p < host port> : <container port>, ports = {<container port> : <host port>}
'''
client = docker.from_env()
cont = client.containers.run('exp/server-mod', 'python s.py', detach=True, ports={'8787/tcp':('127.0.0.1', 8787)}, volumes={'./shared/': {'bind': '/_shared/', 'mode': 'rw'}})
mkfiles(shared, 'file_')

isRunning = False
while not isRunning:
    cont.reload()
    isRunning = cont.attrs['State']['Running']
    print(isRunning)

with socket.create_connection(addr) as sock:
    send_msg(sock, 'test str test str test str 1234567890ABCDEF/,..'.encode())
    try:
        data1 = recv_msg(sock).decode()
        data2 = recv_msg(sock).decode()
        print(data1, data2)
    except AttributeError as err:
        cont.stop()
        print(err)


print('_____________')
print('[SDK] Logs from container')
print(cont.logs().decode())
print('_____________')
