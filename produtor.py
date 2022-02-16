import socket

ip = 'localhost'
porta = 42424

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((ip, porta))

while 1:
    #O valor dos dados deve ser maior que 1 para enviar ao servidor e 
    numero = int(1)
    while numero <= 1 and numero != 0:
        numero = int(input("Digite um valor maior que 1 para receber a soma de todos os números primos menores que ele ou 0 para encerrar a execução:"))

    #Os dados são codificados e enviados ao consumidor
    data = str(numero)
    socket.sendall(str.encode(data))
    data = socket.recv(1024)

    #resposta do consumidor
    print('Mensagem do servidor:', data.decode())
    if numero == 0:
        print("Você optou por encerrar o programa. Até a próxima!")
        break