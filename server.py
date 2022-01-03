import signal
import os
import time
import sys

def readConfiguration(signalNumber, frame):
    print ('(SIGHUP) reading configuration')
    return


def receiveSignal(signalNumber, frame):
    if signalNumber == 2:
        print('Sinal tratado SIGINT -' , signalNumber)
    if signalNumber == 15:        
        print('Sinal tratado SIGTERM -' , signalNumber)
    return

# register the signals to be caught
signal.signal(signal.SIGHUP, readConfiguration)
signal.signal(signal.SIGINT, receiveSignal)
signal.signal(signal.SIGQUIT, receiveSignal)
signal.signal(signal.SIGILL, receiveSignal)
signal.signal(signal.SIGTRAP, receiveSignal)
signal.signal(signal.SIGABRT, receiveSignal)
signal.signal(signal.SIGBUS, receiveSignal)
signal.signal(signal.SIGFPE, receiveSignal)
#signal.signal(signal.SIGKILL, terminateProcess)
signal.signal(signal.SIGUSR1, receiveSignal)
signal.signal(signal.SIGSEGV, receiveSignal)
signal.signal(signal.SIGUSR2, receiveSignal)
signal.signal(signal.SIGPIPE, receiveSignal)
signal.signal(signal.SIGALRM, receiveSignal)
signal.signal(signal.SIGTSTP, receiveSignal)
signal.signal(signal.SIGTERM, receiveSignal)

# Pegando o PID
print('PID:', os.getpid())

# wait in an endless loop for signals 
while True:
    print('Waiting...')
    signal.pause()