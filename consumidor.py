import socket
import math
import os

def primos(N):
   # Input: an integer n > 1.

   # Let A be an array of Boolean values, indexed by integers 2 to n, initially all set to true.
   A = list(range(2, N))

   # for i = 2, 3, 4, ..., not exceeding √n:
   for i in range(2, int(math.sqrt(N)+1)):

      # if A[i] is true:
      if i in A:

         # for j = i2, i2+i, i2+2i, i2+3i, ..., not exceeding n:
         for j in range(i**2, N, i):

            # A[j] := false.
            if j in A: A.remove(j)

   # Output: all i such that A[i] is true.
   return A
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
   mensagemDecodificada = data.decode()
   listaPrimos = primos(int(mensagemDecodificada))
   print(listaPrimos)
   somaPrimos = str(sum(listaPrimos))
   stringPrimos = "O os números primos de 0 até "+mensagemDecodificada+" são "+ "".join(str(listaPrimos)+" e a soma deles é: "+somaPrimos)
   dataRetorno = str.encode(stringPrimos)
   conn.sendall(dataRetorno)