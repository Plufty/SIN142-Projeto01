import socket
import math

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

while 1:
   #A mensagem é recebida e decodificada
   data = conn.recv(1024)
   if not data:
      print('conexão encerrada')
      conn.close()
      break   
   mensagemDecodificada = int(data.decode())

   #Aqui é verificado o conteúdo da mensagem recebida, se for igual a 0 é o sinal para encerrar o a conexão
   if mensagemDecodificada == 0:
      encerramento = "O sinal para encerramento do programa foi recebido. Finalizando programa"
      print(encerramento)
      conn.sendall(str.encode(encerramento))
      conn.close()
      break
   elif mensagemDecodificada > 1:
      #no trecho seguinte, serão calculados os números primos, sua soma e preparada a string de retorno para o cliente
      listaPrimos = primos(mensagemDecodificada)
      print(listaPrimos)
      somaPrimos = str(sum(listaPrimos))
      stringPrimos = "Os números primos menores que "+str(mensagemDecodificada)+" são "+ "".join(str(listaPrimos)+" e a soma deles é: "+somaPrimos)
      
      #A string que será retornada é codificada e enviada
      data = str.encode(stringPrimos)
      conn.sendall(data)