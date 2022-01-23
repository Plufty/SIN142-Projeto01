import signal
import os
import time
import sys
from subprocess import check_output
#Função para adquirir o nome do subprocesso visto que será executado com o comando
# python3 client.py | python3 server.py
def get_pid(name): 
    return int(check_output(["pidof","-s",name]))

print('Capturando o PID do processo para enviar os sinais:')
PID = get_pid("python3") #como está sendo rodado em python3, o subprocesso server assumirá esse nome
print('Enviando sinal de interrupção SIGINT')
time.sleep(3)
os.kill(PID, signal.SIGINT)
print("Enviando sinal SIGTERM")
time.sleep(3)
os.kill(PID, signal.SIGTERM)
print("Finalizando o processo SIGKILL")
time.sleep(3)
os.kill(PID, signal.SIGKILL)
