import socket

ip = 'localhost'
porta = 42424

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((ip, porta))

numero = input()
socket.sendall(str.encode(numero))
data = socket.recv(1024)


print('Mensagem ecoada:', data.decode())