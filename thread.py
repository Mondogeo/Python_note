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
    print('Main terminato')

'''
--->
Avvio modulo main
Avvio thread thread2 con ritardo di 2
Main terminato
Thread secondario terminato
'''
    

