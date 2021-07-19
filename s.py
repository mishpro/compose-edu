import socket
from recvall import recv_msg, send_msg

address = ('', 8787)
sock = socket.socket()
sock.bind(address)
sock.listen(1)
conn, addr = sock.accept()
print('Connected: ', addr)


data = recv_msg(conn).decode()
print(data)
send_msg(conn, data.upper().encode())
conn.close()
sock.close()
