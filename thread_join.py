
'''
Multithreading con attesa della fine del Thread

In questo caso l'uso di Join impedisce al main di
terminare prima che il thread secondario sia terminato anchesso
'''
import threading #importo il modulo threading
import time
def mythread (nome, ritardo): #definisco il secondo thread
    print(f'Avvio thread {nome} con ritardo di {ritardo}')
    time.sleep(ritardo)
    print('Thread secondario terminato')

if __name__=='__main__': #avvio il __main__
    print ('Avvio modulo main')
    #definisco l'oggetto thread
    th=threading.Thread(target=mythread, args=('thread2', 2)) #definisco il thread secondario ed i parametri
    th.start() #avvio il thread secondario
    th.join() #impongo che anche il main non termini prima del secondo thread
    print('Main terminato')

'''
--->
Avvio modulo main
Avvio thread thread2 con ritardo di 2
Thread secondario terminato
Main terminato **> il main si è fermato ad attendere la fine del thread secondario prima di terminare
'''
    

