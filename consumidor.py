import socket
import math
import os

def primos(N):#Função para definir os números primos até o número passado
   A = list(range(2, N)) # a lista inicia de 2 que é o primeiro número primo
   for i in range(2, int(math.sqrt(N)+1)):
      if i in A:
         for j in range(i**2, N, i):
            if j in A: A.remove(j)
   return A #retorna a lista dos números primos de 2 até o número passado.
ip = 'localhost'
porta = 42424

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((ip, porta))
socket.listen()
print('Esperando a conexão')
conn, ender = socket.accept()

print('conectado em', ender)
PID = os.getpid()
print(PID)

while 1:
   data = conn.recv(1024)
   if not data:
      print('conexão encerrada')
      conn.close()
      break   
   mensagemDecodificada = int(data.decode())

   if mensagemDecodificada == 0: #se o inteiro recebido for igual a 0, é um sinal para encerrar o processo
      encerramento = "O sinal para encerramento do programa foi recebido. Finalizando programa"
      print(encerramento)
      conn.sendall(str.encode(encerramento))
      break   

   listaPrimos = primos(mensagemDecodificada)
   print(listaPrimos)
   somaPrimos = str(sum(listaPrimos))
   stringPrimos = "O os números primos de 0 até "+str(mensagemDecodificada)+" são "+ "".join(str(listaPrimos)+" e a soma deles é: "+somaPrimos)
   dataRetorno = str.encode(stringPrimos)
   conn.sendall(dataRetorno)