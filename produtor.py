import socket

ip = 'localhost'
porta = 42424

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((ip, porta))

numero = int(1)
while numero <= 1 and numero != 0:
    print("Digite um valor maior que 1 para receber a soma de todos os números primos até ele ou 0 para encerrar a execução:")
    numero = int(input())

data = str(numero)
socket.sendall(str.encode(data))
data = socket.recv(1024)


print('Mensagem do servidor:', data.decode())