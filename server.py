import signal
import os
import time
import sys

def tratarSinal(signalNumber, frame): #Sinais tratados SIGINT-2 e SIGTERM-15
    if signalNumber == 2:
        print('Sinal tratado SIGINT -' , signalNumber)
    if signalNumber == 15:        
        print('Sinal tratado SIGTERM -' , signalNumber)
    return

signal.signal(signal.SIGINT, tratarSinal)
signal.signal(signal.SIGTERM, tratarSinal)

# Pegando o PID
print('PID:', os.getpid())

#esperando em um loop infinito
while True:
    print('Esperando sinal...')
    signal.pause() 