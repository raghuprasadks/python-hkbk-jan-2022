import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))
print('hi from client')
msg=s.recv(1024)
print(msg.decode("utf-8"))