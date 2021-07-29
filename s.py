import socket
import os

from recvall import recv_msg, send_msg

address = ('', 8787)
# sock = socket.socket()
# sock.bind(address)
# sock.listen(1)
with socket.create_server(address) as sock:
    conn, addr = sock.accept()
    print('Connected: ', addr)
    data = recv_msg(conn).decode()
    print(data)
    send_msg(conn, data.upper().encode())
    send_msg(conn, str(os.listdir('/_shared/')).encode())
    conn.close()
