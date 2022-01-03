import signal
import os
import time
import sys
print('Digite o PID do processo para enviar os sinais:')
PID = int(input())
print('Enviando sinal de interrupção SIGINT')
time.sleep(3)
os.kill(PID, signal.SIGINT)
print("Enviando sinal SIGTERM")
time.sleep(3)
os.kill(PID, signal.SIGTERM)
print("Finalizando o processo SIGKILL")
time.sleep(3)
os.kill(PID, signal.SIGKILL)
